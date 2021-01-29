#!/usr/bin/env python3
"""
This script is part of our study on Oxford Nanopore preps and small plasmids. See here for more
information: https://github.com/rrwick/Small-plasmid-Nanopore

It takes two inputs: a directory containing assemblies and a file with read alignment information.
The latter can either be a table made by the assign_reads.py script (for ONT reads) or a sorted
BAM file (for Illumina reads). It outputs the average read depth for each replicon in the
assemblies, with cross-replicon repeats masked out.

Copyright 2021 Ryan Wick (rrwick@gmail.com)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version. This program is distributed in the hope that it
will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should
have received a copy of the GNU General Public License along with this program. If not, see
<https://www.gnu.org/licenses/>.
"""

import argparse
import glob
import gzip
import os
import pathlib
import statistics
import subprocess
import sys
import tempfile


def get_arguments():
    parser = argparse.ArgumentParser(description='Get per-replicon depths')

    parser.add_argument('assemblies_dir', type=str,
                        help='Directory containing FASTA files of the assemblies')
    parser.add_argument('read_table_or_bam', type=str,
                        help='Read table file made by assign_reads.py or a sorted BAM file')

    parser.add_argument('--no_mask', action='store_true',
                        help='Turn off repeat masking')

    parser.add_argument('--identity', type=float, default=95,
                        help='Only mask regions with this much or more alignment identity')
    parser.add_argument('--threads', type=int, default=12,
                        help='Threads used in alignments')

    args = parser.parse_args()
    return args


def main():
    args = get_arguments()

    if args.no_mask:
        replicon_lengths = get_replicon_lengths(args.assemblies_dir)
        masked_bases = {r: [] for r in replicon_lengths.keys()}
    else:
        masked_bases, replicon_lengths = get_masked_regions(args.assemblies_dir, args.threads, args.identity)
    
    if args.read_table_or_bam.endswith('.bam'):
        depths = get_depths_from_bam(args.read_table_or_bam, replicon_lengths)
    else:
        depths = get_depths_from_table(args.read_table_or_bam, replicon_lengths)

    for replicon_name, base_depths in depths.items():
        replicon_length = replicon_lengths[replicon_name]
        unmasked_depths = []
        for i, depth in enumerate(base_depths):
            if i not in masked_bases[replicon_name]:
                unmasked_depths.append(depth)
        try:
            mean_depth = statistics.mean(unmasked_depths)
        except statistics.StatisticsError:
            mean_depth = 'NA'
        print(f'{replicon_name}\t{replicon_length}\t{len(unmasked_depths)}\t{mean_depth}')


def get_replicon_lengths(assemblies_dir):
    replicon_lengths = {}
    for ref_filename in sorted(glob.glob(assemblies_dir + '/*.fasta')):
        for replicon_name, replicon_seq in load_fasta(ref_filename):
            replicon_lengths[replicon_name] = len(replicon_seq)
    return replicon_lengths


def get_masked_regions(assemblies_dir, threads, identity):
    replicons = []
    replicon_lengths = {}
    alignments = []

    with tempfile.TemporaryDirectory() as temp_dir:
        for ref_filename in sorted(glob.glob(assemblies_dir + '/*.fasta')):
            genome_name = pathlib.Path(ref_filename).name.replace('.fasta', '')
            for replicon_name, replicon_seq in load_fasta(ref_filename):
                replicons.append(replicon_name)
                replicon_lengths[replicon_name] = len(replicon_seq)
                temp_fasta_filename = pathlib.Path(temp_dir) / (replicon_name + '.fasta')
                with open(temp_fasta_filename, 'wt') as temp_fasta:
                    temp_fasta.write(f'>{replicon_name}\n{replicon_seq}\n')

        replicon_fastas = sorted(glob.glob(temp_dir + '/*.fasta'))
        for i, a in enumerate(replicon_fastas):
            a_name = pathlib.Path(a).name.replace('.fasta', '')
            a_name_no_version = a_name.replace('_v1', '').replace('_v2', '')
            for j in range(i+1, len(replicon_fastas)):
                b = replicon_fastas[j]
                b_name = pathlib.Path(b).name.replace('.fasta', '')
                b_name_no_version = b_name.replace('_v1', '').replace('_v2', '')

                # Don't align two different versions of the same plasmid to each other.
                if a_name_no_version == b_name_no_version:
                    continue

                minimap2_command = ['minimap2', '-c', '-x', 'map-ont', '-t', str(threads),
                                    str(a), str(b)]
                with open(os.devnull, 'wb') as dev_null:
                    alignment_output = subprocess.check_output(minimap2_command,
                                                               stderr=dev_null).decode()

                new_alignments = [Alignment(line) for line in alignment_output.splitlines()]
                new_alignments = [a for a in new_alignments if a.percent_identity >= identity]

                plural = '' if len(new_alignments) == 1 else 's'
                print(f'{a_name} vs {b_name}: {len(new_alignments)} alignment{plural}')

                alignments += new_alignments

    masked_bases = {r: set() for r in replicons}
    for a in alignments:
        for i in range(a.query_start, a.query_end):
            masked_bases[a.query_name].add(i)
        for i in range(a.ref_start, a.ref_end):
            masked_bases[a.ref_name].add(i)

    print('\n\nMasked bases:')
    for r in replicons:
        length = replicon_lengths[r]
        masked_length = len(masked_bases[r])
        masked_percent = 100.0 * masked_length / length
        print(f'{r} ({length:,} bp): {masked_length:,} bp masked ({masked_percent:.1f}%)')

    return masked_bases, replicon_lengths


def get_depths_from_bam(filename, replicon_lengths):
    print('\nRunnings samtools depth')
    depths = {}
    for rep_name, rep_length in replicon_lengths.items():
        depths[rep_name] = [0] * rep_length

    genome_name = pathlib.Path(filename).name.replace('.bam', '')

    depth_command = ['samtools', 'depth', filename]
    with open(os.devnull, 'wb') as dev_null:
        depth_output = subprocess.check_output(depth_command, stderr=dev_null).decode()

    for line in depth_output.splitlines():
        parts = line.strip().split('\t')
        rep_name = parts[0]
        depths[rep_name][int(parts[1])-1] = int(parts[2])

    print()
    return depths


def get_depths_from_table(filename, replicon_lengths):
    print('\nReading table lines:')
    depths = {}
    for rep_name, rep_length in replicon_lengths.items():
        depths[rep_name] = [0] * rep_length

    line_num = 0
    with get_open_func(filename)(filename, 'rt') as table:
        for line in table:
            parts = line.strip().split('\t')
            alignments_column = parts[13]
            if alignments_column == 'alignments':  # header
                continue
            alignment_strings = alignments_column.split(',')
            for a in alignment_strings:
                if not a:
                    continue
                a_parts = a.split(':')
                rep_name = a_parts[1]
                rep_length = replicon_lengths[rep_name]
                rep_range = a_parts[2].split('(')[0].split('-')
                rep_start, rep_end = int(rep_range[0]), int(rep_range[1])

                for i in range(rep_start, rep_end):
                    if i >= rep_length:
                        i -= rep_length
                    depths[rep_name][i] += 1
            line_num += 1
            print(f'\r{line_num}', end='')
    print()

    return depths


def load_fasta(fasta_filename, include_full_header=False):
    if get_compression_type(fasta_filename) == 'gz':
        open_func = gzip.open
    else:  # plain text
        open_func = open
    fasta_seqs = []
    with open_func(fasta_filename, 'rt') as fasta_file:
        name = ''
        sequence = []
        for line in fasta_file:
            line = line.strip()
            if not line:
                continue
            if line[0] == '>':  # Header line = start of new contig
                if name:
                    if include_full_header:
                        fasta_seqs.append((name.split()[0], name, ''.join(sequence)))
                    else:
                        fasta_seqs.append((name.split()[0], ''.join(sequence)))
                    sequence = []
                name = line[1:]
            else:
                sequence.append(line)
        if name:
            if include_full_header:
                fasta_seqs.append((name.split()[0], name, ''.join(sequence)))
            else:
                fasta_seqs.append((name.split()[0], ''.join(sequence)))
    return fasta_seqs


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
            if parts[0] == 'filename':  # header line
                header = parts
            else:
                read_name = parts[1]
                data[read_name] = parts
                all_read_names.append(read_name)
    return header, data, sorted(all_read_names)


class Alignment(object):

    def __init__(self, paf_line):
        line_parts = paf_line.strip().split('\t')
        if len(line_parts) < 11:
            sys.exit('Error: alignment file does not seem to be in PAF format')

        self.query_name = line_parts[0]
        self.query_length = int(line_parts[1])
        self.query_start = int(line_parts[2])
        self.query_end = int(line_parts[3])
        self.strand = line_parts[4]

        self.ref_name = line_parts[5]
        self.ref_length = int(line_parts[6])
        self.ref_start = int(line_parts[7])
        self.ref_end = int(line_parts[8])

        self.matching_bases = int(line_parts[9])
        self.num_bases = int(line_parts[10])
        self.percent_identity = 100.0 * self.matching_bases / self.num_bases

        self.query_align_len = self.query_end - self.query_start
        self.query_cov = 100.0 * self.query_align_len / self.query_length

        ref_name_parts = self.ref_name.split('__')
        if len(ref_name_parts) != 2:
            sys.exit('Error: reference names must be in the form of genome_name__replicon_name')


    def __repr__(self):
        return str(self.query_start) + '-' + str(self.query_end) + \
               '(' + self.strand + '):' + \
               self.ref_name + ':' + str(self.ref_start) + '-' + str(self.ref_end) + \
               '(' + ('%.3f' % self.percent_identity) + '%)'



if __name__ == '__main__':
    main()
