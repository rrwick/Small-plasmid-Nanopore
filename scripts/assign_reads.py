#!/usr/bin/env python3
"""
This script is part of our study on Oxford Nanopore preps and small plasmids. See here for more
information: https://github.com/rrwick/Small-plasmid-Nanopore

It takes three inputs: a file of ONT reads, a Guppy sequencing summary file and a file of
alignments made by the align_reads.py script. It outputs a table of summary information for each
read in the ONT set.

Copyright 2020 Ryan Wick (rrwick@gmail.com)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version. This program is distributed in the hope that it
will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should
have received a copy of the GNU General Public License along with this program. If not, see
<https://www.gnu.org/licenses/>.
"""

import argparse
import collections
import glob
import gzip
import statistics
import sys


def get_arguments():
    parser = argparse.ArgumentParser(description='Assign reads to reference')

    parser.add_argument('reads', type=str,
                        help='FASTQ read filename')
    parser.add_argument('seq_summary', type=str,
                        help='Guppy sequencing summary file (with read name in first column)')
    parser.add_argument('paf_filename', type=str,
                        help='PAF file made by minimap2 aligning reads to reference FASTA')

    parser.add_argument('--min_align_id', type=float, default=75.0,
                        help='Alignments with a lower identity than this will be discarded')
    parser.add_argument('--min_align_len', type=int, default=100,
                        help='Alignments shorter than this will be discarded')

    parser.add_argument('--min_read_id', type=float, default=80.0,
                        help='Reads with a lower identity than this will not be processed')
    parser.add_argument('--min_read_cov', type=float, default=50.0,
                        help='Reads with less than this much coverage will not be processed')

    args = parser.parse_args()
    return args


def main():
    args = get_arguments()
    read_lengths = load_read_lengths(args.reads)
    seq_summary_header, seq_summary_data, all_read_names = load_seq_summary(args.seq_summary)
    alignments_by_read = load_alignments(args.paf_filename)

    # Some sanity checks
    assert len(read_lengths) == len(seq_summary_data)
    assert len(alignments_by_read) <= len(read_lengths)

    print_header(seq_summary_header)

    for read_name in all_read_names:
        alignments = alignments_by_read[read_name]
        read_length = read_lengths[read_name]
        process_read(read_length, alignments,
                     args.min_align_id, args.min_align_len, args.min_read_id, args.min_read_cov,
                     seq_summary_data[read_name], seq_summary_header)


def print_header(seq_summary_header):
    print('\t'.join(seq_summary_header), end='\t')
    print('\t'.join(['read_length', 'mean_identity', 'read_coverage',
                     'unaligned_start', 'unaligned_end', 'total_unaligned',
                     'alignments', 'reference_names',
                     'chimera', 'within_bin_chimera', 'cross_bin_chimera', 'demultiplex_status']))


def process_read(read_length, alignments, min_align_id, min_align_len, min_read_id, min_read_cov,
                 seq_summary_data, seq_summary_header):
    if alignments:
        assert read_length == alignments[0].read_length  # sanity check

    alignments = [a for a in alignments
                  if a.percent_identity >= min_align_id and a.read_align_len >= min_align_len]
    alignments = cull_redundant_alignments(alignments)

    identities = [0.0] * read_length
    references = [None] * read_length
    for a in alignments:
        ref_name_no_version = a.ref_name.replace('_v1', '').replace('_v2', '')
        for i in range(a.read_start, a.read_end):
            if a.percent_identity > identities[i]:
                identities[i] = a.percent_identity
                references[i] = ref_name_no_version

    # If the read has low identity or coverage, we wipe it clean so it's not considered for
    # chimera or demux calls.
    mean_identity = get_mean_identity(identities)
    coverage = get_coverage(identities)
    if mean_identity < min_read_id or coverage < min_read_cov:
        identities = [0.0] * read_length
        references = [None] * read_length

    total_unaligned, unaligned_start, unaligned_end = count_unaligned_bases(identities)
    reference_bases = get_reference_bases(references)
    reference_names = sorted(reference_bases.keys())
    chimera, cross_bin_chimera, within_bin_chimera = get_chimera_types(reference_names)
    demux_status = get_demux_status(seq_summary_data, seq_summary_header, reference_names)

    if 'chimera' in demux_status:
        assert cross_bin_chimera == 'yes'  # sanity check

    print('\t'.join(seq_summary_data), end='\t')

    reference_names_str = ','.join(reference_names)
    alignments_str = ','.join(str(x) for x in alignments)

    print(f'{read_length}\t{mean_identity:.1f}%\t{coverage:.1f}%\t'
          f'{unaligned_start}\t{unaligned_end}\t{total_unaligned}\t'
          f'{alignments_str}\t{reference_names_str}\t'
          f'{chimera}\t{within_bin_chimera}\t{cross_bin_chimera}\t{demux_status}')


def cull_redundant_alignments(alignments):
    if not alignments:
        return alignments

    alignments = sorted(alignments, key=lambda x: x.matching_bases, reverse=True)
    best_alignment = alignments[0]

    # We assume that there's not too much variation in alignment identity across a read, so we
    # throw out any alignments which are too much worse than the best.
    min_align_id = best_alignment.percent_identity * 0.9
    alignments = [a for a in alignments if a.percent_identity >= min_align_id]

    # To reduce the number of false positive chimera calls, we assume the best alignment is the
    # true reference sequence and prefer alignments to that sequence when culling redundancy.
    same_as_best = [a for a in alignments if a.ref_name == best_alignment.ref_name]
    other_than_best = [a for a in alignments if a.ref_name != best_alignment.ref_name]
    same_as_best = sorted(same_as_best, key=lambda x: x.matching_bases, reverse=True)
    other_than_best = sorted(other_than_best, key=lambda x: x.matching_bases, reverse=True)
    alignments = same_as_best + other_than_best

    filtered_alignments = []
    for a in alignments:
        if not overlapping(a, filtered_alignments):
            filtered_alignments.append(a)

    return sorted(filtered_alignments, key=lambda x: x.read_start)


def overlapping(alignment, existing_alignments):
    for existing_alignment in existing_alignments:
        if alignments_overlap(alignment, existing_alignment):
            return True
    return False


def alignments_overlap(a, b):
    if a.read_start <= b.read_end and b.read_start <= a.read_end:  # There is some overlap
        allowed_overlap_size = 100
        allowed_overlap_fraction = 0.8
        overlap_size = len(range(max(a.read_start, b.read_start),
                                 min(a.read_end, b.read_end) + 1))
        a_overlap_fraction = overlap_size / (a.read_end - a.read_start)
        b_overlap_fraction = overlap_size / (b.read_end - b.read_start)
        if a_overlap_fraction > allowed_overlap_fraction:
            return True
        if b_overlap_fraction > allowed_overlap_fraction:
            return True
        return overlap_size > allowed_overlap_size
    else:
        return False


def count_unaligned_bases(identities):
    aligned_count = sum(1 if i > 0.0 else 0 for i in identities)
    total_unaligned_bases = len(identities) - aligned_count
    unaligned_start = 0
    for i in identities:
        if i == 0.0:
            unaligned_start += 1
        else:
            break
    unaligned_end = 0
    for i in identities[::-1]:
        if i == 0.0:
            unaligned_end += 1
        else:
            break
    return total_unaligned_bases, unaligned_start, unaligned_end


def get_coverage(identities):
    aligned_count = sum(1 if i > 0.0 else 0 for i in identities)
    coverage = aligned_count / len(identities)
    return 100.0 * coverage


def get_mean_identity(identities):
    try:
        return statistics.mean(i for i in identities if i != 0.0)
    except statistics.StatisticsError:
        return 0.0


def get_reference_bases(references):
    reference_bases = collections.defaultdict(int)
    for r in references:
        if r is not None:
            reference_bases[r] += 1
    return reference_bases


def get_chimera_types(reference_names):
    chimera = 'yes' if len(reference_names) > 1 else 'no'

    per_genome = collections.defaultdict(int)
    for r in reference_names:
        genome_name = r.split('__')[0]
        per_genome[genome_name] += 1

    cross_bin_chimera = 'yes' if len(per_genome) > 1 else 'no'
    within_bin_chimera = 'yes' if any(count > 1 for count in per_genome.values()) else 'no'

    return chimera, cross_bin_chimera, within_bin_chimera


def get_demux_status(seq_summary_data, seq_summary_header, reference_names):
    guppy_barcode = seq_summary_data[seq_summary_header.index('barcode_arrangement')]
    actual_barcode = get_actual_barcode(reference_names)

    if actual_barcode == 'chimera':
        if guppy_barcode == 'unclassified':
            return 'chimera_unclassified'
        else:
            return 'chimera_classified'

    if actual_barcode == 'unaligned':
        if guppy_barcode == 'unclassified':
            return 'unaligned_unclassified'
        else:
            return 'unaligned_classified'

    if guppy_barcode == 'unclassified':
        return 'unclassified'

    assert guppy_barcode.startswith('barcode')
    assert actual_barcode.startswith('barcode')

    if guppy_barcode == actual_barcode:
        return 'correct'
    else:
        return 'incorrect'


def get_actual_barcode(reference_names):
    genome_names = set([r.split('__')[0] for r in reference_names])
    if len(genome_names) > 1:
        return 'chimera'
    if len(genome_names) == 0:
        return 'unaligned'
    genome_name = list(genome_names)[0]
    if genome_name == 'Acinetobacter_baumannii_J9':
        return 'barcode01'
    if genome_name == 'Citrobacter_koseri_MINF_9D':
        return 'barcode02'
    if genome_name == 'Enterobacter_kobei_MSB1_1B':
        return 'barcode03'
    if genome_name == 'Haemophilus_M1C132_1' or genome_name == 'Haemophilus_unknown_M1C132_1':
        return 'barcode04'
    if genome_name == 'Klebsiella_oxytoca_MSB1_2C':
        return 'barcode05'
    if genome_name == 'Klebsiella_variicola_INF345':
        return 'barcode07'
    if genome_name == 'Serratia_marcescens_17-147-1671':
        return 'barcode08'
    assert False


def get_compression_type(filename):
    """
    Attempts to guess the compression (if any) on a file using the first few bytes.
    http://stackoverflow.com/questions/13044562
    """
    magic_dict = {'gz': (b'\x1f', b'\x8b', b'\x08'),
                  'bz2': (b'\x42', b'\x5a', b'\x68'),
                  'zip': (b'\x50', b'\x4b', b'\x03', b'\x04')}
    max_len = max(len(x) for x in magic_dict)
    unknown_file = open(str(filename), 'rb')
    file_start = unknown_file.read(max_len)
    unknown_file.close()
    compression_type = 'plain'
    for file_type, magic_bytes in magic_dict.items():
        if file_start.startswith(magic_bytes):
            compression_type = file_type
    if compression_type == 'bz2':
        sys.exit('Error: cannot use bzip2 format - use gzip instead')
    if compression_type == 'zip':
        sys.exit('Error: cannot use zip format - use gzip instead')
    return compression_type


def get_open_func(filename):
    if get_compression_type(filename) == 'gz':
        return gzip.open
    else:  # plain text
        return open


def load_seq_summary(filename):
    header, data, all_read_names = [], {}, []
    with get_open_func(filename)(filename, 'rt') as summary:
        for line in summary:
            parts = line.strip().split('\t')
            if parts[0] == 'filename' or parts[0] == 'read_id':  # header line
                header = parts
            else:
                read_name = parts[0]
                data[read_name] = parts
                all_read_names.append(read_name)
    return header, data, sorted(all_read_names)


def load_alignments(filename):
    alignments_by_read = collections.defaultdict(list)
    with get_open_func(filename)(filename, 'rt') as paf:
        for line in paf:
            a = Alignment(line)
            alignments_by_read[a.read_name].append(a)
    return alignments_by_read


def load_read_lengths(filename):
    read_lengths = {}
    with get_open_func(filename)(filename, 'rt') as fastq:
        for line in fastq:
            name = line.strip()[1:].split()[0]
            sequence = next(fastq).strip()
            next(fastq)
            next(fastq)
            read_lengths[name] = len(sequence)
    return read_lengths


class Alignment(object):

    def __init__(self, paf_line):
        line_parts = paf_line.strip().split('\t')
        if len(line_parts) < 11:
            sys.exit('Error: alignment file does not seem to be in PAF format')

        self.read_name = line_parts[0]
        self.read_length = int(line_parts[1])
        self.read_start = int(line_parts[2])
        self.read_end = int(line_parts[3])
        self.strand = line_parts[4]

        self.ref_name = line_parts[5]
        self.ref_length = int(line_parts[6])
        self.ref_start = int(line_parts[7])
        self.ref_end = int(line_parts[8])

        self.matching_bases = int(line_parts[9])
        self.num_bases = int(line_parts[10])
        self.percent_identity = 100.0 * self.matching_bases / self.num_bases

        self.read_align_len = self.read_end - self.read_start
        self.read_cov = 100.0 * self.read_align_len / self.read_length

        ref_name_parts = self.ref_name.split('__')
        if len(ref_name_parts) != 2:
            sys.exit('Error: reference names must be in the form of genome_name__replicon_name')

        # self.cigar = None
        # for part in line_parts:
        #     if part.startswith('cg:Z:'):
        #         self.cigar = part[5:]
        #
        # self.alignment_score = None
        # for part in line_parts:
        #     if part.startswith('AS:i:'):
        #         self.alignment_score = int(part[5:])

    def __repr__(self):
        return str(self.read_start) + '-' + str(self.read_end) + \
               '(' + self.strand + '):' + \
               self.ref_name + ':' + str(self.ref_start) + '-' + str(self.ref_end) + \
               '(' + ('%.3f' % self.percent_identity) + '%)'


if __name__ == '__main__':
    main()
