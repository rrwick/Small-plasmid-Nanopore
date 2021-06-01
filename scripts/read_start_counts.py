#!/usr/bin/env python3
"""
This script is part of our study on Oxford Nanopore preps and small plasmids. See here for more
information: https://github.com/rrwick/Small-plasmid-Nanopore

It takes four inputs: a directory containing assemblies, an output directory, a sequence window
size and tables with read alignment information.

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
import collections
import glob
import gzip
import math
import os
import pathlib
import random
import statistics
import subprocess
import sys
import tempfile

from scipy.stats import poisson


def get_arguments():
    parser = argparse.ArgumentParser(description='Get per-window read-start counts')

    parser.add_argument('assemblies_dir', type=str,
                        help='Directory containing FASTA files of the assemblies')
    parser.add_argument('out_dir', type=str,
                        help='Directory to save tables')
    parser.add_argument('window_size', type=int,
                        help='Window size for read-start counts')
    parser.add_argument('read_tables', type=str, nargs='+',
                        help='Read table file made by assign_reads.py')

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
    out_dir = make_out_dir(args.out_dir)

    replicon_lengths = get_replicon_lengths(args.assemblies_dir)
    if args.no_mask:
        masked_bases = {r: [] for r in replicon_lengths.keys()}
    else:
        masked_bases = get_masked_regions(args.assemblies_dir, args.threads, args.identity)
    start_positions = get_start_positions_from_tables(args.read_tables, replicon_lengths)

    print('\n\n\n')
    print('rep_name\tmean_read_starts_per_window\tsig_threshold\tneg_log10_sig_threshold')
    for rep_name in sorted(start_positions.keys()):
        process_one_replicon(rep_name, replicon_lengths[rep_name], masked_bases[rep_name],
                             start_positions[rep_name], args.window_size, out_dir)


def make_out_dir(out_dir):
    out_dir = pathlib.Path(out_dir)
    if out_dir.is_dir() or out_dir.is_file():
        sys.exit(f'Error: {out_dir} already exists')
    out_dir.mkdir()
    return out_dir


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

    return masked_bases


def get_start_positions_from_tables(filenames, replicon_lengths):
    start_positions = collections.defaultdict(list)

    for filename in filenames:
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
                    strand = a_parts[0][-2]
                    rep_name = a_parts[1]
                    rep_length = replicon_lengths[rep_name]
                    rep_range = a_parts[2].split('(')[0].split('-')
                    rep_start, rep_end = int(rep_range[0]), int(rep_range[1])
                    if strand == '+':
                        pos = rep_start
                    elif strand == '-':
                        pos = rep_end
                    else:
                        assert False
                    while pos >= rep_length:
                        pos -= rep_length
                    start_positions[rep_name].append(pos)

    return start_positions


def process_one_replicon(rep_name, replicon_length, masked_bases, start_positions, window_size, out_dir):
    random.shuffle(start_positions)
    start_position_count = len(start_positions) // 2
    start_positions = start_positions[:start_position_count]



    read_starts_per_window = get_read_starts_per_window(replicon_length, window_size, start_positions)

    all_read_starts = []
    for window, read_starts in read_starts_per_window.items():
        masked_window = False
        for i in range(window, window+window_size):
            if i in masked_bases:
                masked_window = True
        if not masked_window:
            all_read_starts.append(read_starts)
    mean_read_starts_per_window = statistics.mean(all_read_starts)
    sig_threshold = 0.05 / len(all_read_starts)
    neg_log10_sig_threshold = -math.log10(sig_threshold)

    print(f'{rep_name}\t{mean_read_starts_per_window}\t{sig_threshold}\t{neg_log10_sig_threshold}')

    out_filename = out_dir / (rep_name + '.tsv')
    with open(out_filename, 'wt') as out_file:
        out_file.write('window\tread_starts\tp_val\tneg_log10_p_val\tsigned_neg_log10_p_val\n')
        for window, read_starts in read_starts_per_window.items():
            masked_window = False
            for i in range(window, window+window_size):
                if i in masked_bases:
                    masked_window = True

            # High numbers of read-starts
            if read_starts > mean_read_starts_per_window:
                p_val = poisson.sf(read_starts-1, mean_read_starts_per_window)
                try:
                    neg_log10_p_val = -math.log10(p_val)
                    signed_neg_log10_p_val = neg_log10_p_val
                except ValueError:
                    neg_log10_p_val = 'inf'
                    signed_neg_log10_p_val = 'inf'

            # Low numbers of read-starts
            else:
                p_val = poisson.cdf(read_starts, mean_read_starts_per_window)
                try:
                    neg_log10_p_val = -math.log10(p_val)
                    signed_neg_log10_p_val = -neg_log10_p_val
                except ValueError:
                    neg_log10_p_val = 'inf'
                    signed_neg_log10_p_val = '-inf'

            if not masked_window:
                out_file.write(f'{window}\t{read_starts}\t{p_val}\t{neg_log10_p_val}\t{signed_neg_log10_p_val}\n')
            else:
                out_file.write(f'{window}\t{read_starts}\tn/a\tn/a\tn/a\n')


def get_read_starts_per_window(replicon_length, window_size, start_positions):
    """
    Takes in a list of read-start positions and outputs a dictionary of read-start counts per window.
    """
    read_starts_per_window = {window: 0 for window in range(0, replicon_length - window_size, window_size)}
    for p in start_positions:
        window = int(p / window_size) * window_size
        try:
            read_starts_per_window[window] += 1
        except KeyError:
            pass
    return read_starts_per_window


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
