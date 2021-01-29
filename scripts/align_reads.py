#!/usr/bin/env python3
"""
This script is part of our study on Oxford Nanopore preps and small plasmids. See here for more
information: https://github.com/rrwick/Small-plasmid-Nanopore

It takes a read file and multiple completed assemblies as input. It then independently aligns all
reads to each replicon in the assemblies and outputs the alignments. The replicons are doubled
before alignment to allow for alignments over the start/end junction in circular sequences.

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
import pathlib
import subprocess
import sys
import tempfile


def get_arguments():
    parser = argparse.ArgumentParser(description='Align reads to doubled references')

    parser.add_argument('reads', type=str,
                        help='FASTQ read filename')
    parser.add_argument('assemblies', type=str, nargs='+',
                        help='FASTA files of the assemblies')

    parser.add_argument('--threads', type=int, default=32,
                        help='Threads used in minimap2 alignments')

    args = parser.parse_args()
    return args


def main():
    args = get_arguments()
    print(f'aligning reads to: {args.assemblies}', file=sys.stderr)
    for ref_filename in args.assemblies:
        print('\n\n\n\n', file=sys.stderr)
        print(ref_filename, file=sys.stderr)
        print('================================================================================', file=sys.stderr)
        for replicon_name, replicon_seq in load_fasta(ref_filename):
            print('\n' + replicon_name, file=sys.stderr)
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_fasta_filename = pathlib.Path(temp_dir) / 'temp.fasta'
                with open(temp_fasta_filename, 'wt') as temp_fasta:
                    temp_fasta.write(f'>{replicon_name}\n{replicon_seq}{replicon_seq}\n')
                minimap2_command = ['minimap2', '-c', '-x', 'map-ont', '-t', str(args.threads), str(temp_fasta_filename), str(args.reads)]
                subprocess.run(minimap2_command)


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


if __name__ == '__main__':
    main()
