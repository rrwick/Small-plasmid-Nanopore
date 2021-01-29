#!/usr/bin/env python3
"""
This script is part of our study on Oxford Nanopore preps and small plasmids. See here for more
information: https://github.com/rrwick/Small-plasmid-Nanopore

It takes a completed assembly and a BAM of Illumina reads as input. It then steps through the
assembly's chromosome in 1000 bp windows (adjustable via the --window parameter) and outputs the
GC and read depth for each window. The read depths are normalised to the 50% GC depth.

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

    parser.add_argument('assembly', type=str,
                        help='FASTA files of the assembly')
    parser.add_argument('bam', type=str,
                        help='A sorted BAM file')

    parser.add_argument('--window', type=int, default=1000,
                        help='Window size for depth/GC measurements')

    args = parser.parse_args()
    return args


def main():
    args = get_arguments()

    seqs = load_fasta(args.assembly)
    replicon_lengths = {name: len(seq) for name, seq in seqs}
    depths = get_depths_from_bam(args.bam, replicon_lengths)

    half_window = args.window // 2

    gc_and_depths = []
    for name, seq in seqs:
        if 'chromosome' not in name:
            continue
        for i in list(range(args.window, len(seq)-args.window, args.window)):
            range_min = i - half_window
            range_max = i + half_window
            window_seq = seq[range_min:range_max]
            window_depth = statistics.mean(depths[name][range_min:range_max])
            gc = get_seq_gc(window_seq)
            gc_and_depths.append((gc, window_depth))

    fifty_gc_depths = [depth for gc, depth in gc_and_depths if 49 <= gc <= 51]
    fifty_gc_mean_depth = statistics.mean(fifty_gc_depths)
    normalised_gc_and_depths = [(gc, depth / fifty_gc_mean_depth) for gc, depth in gc_and_depths]
    
    for gc, depth in normalised_gc_and_depths:
        print(f'{gc}\t{depth}')


def get_seq_gc(seq):
    seq = seq.upper()
    total_bases = len(seq)
    a_count = seq.count('A')
    c_count = seq.count('C')
    g_count = seq.count('G')
    t_count = seq.count('T')
    assert a_count + c_count + g_count + t_count == total_bases
    return 100.0 * (c_count + g_count) / total_bases


def get_depths_from_bam(filename, replicon_lengths):
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


if __name__ == '__main__':
    main()
