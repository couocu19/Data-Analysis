#! /usr/bin/env python3
# Converts a GFA assembly graph to a FASTA file of all sequences
# within the graph. Notably, this ignores connections between sequences
# in the graph.
#
# Depends on Python 3.6 or later.
#
# Usage:
# $ ./gfa_to_fasta.py mygraph.gfa contigs.fasta
# python3 gfa_to_fasta.py CPC.Phase1.CHM13v2-full.gfa hmgfa.fasta

import sys

# IN_FILENAME = sys.argv[1]
# OUT_FILENAME = sys.argv[2]
IN_FILENAME = sys.argv[1]
OUT_FILENAME = sys.argv[2]

print(f"Converting GFA {IN_FILENAME} --> FASTA {OUT_FILENAME}...")

num_seqs = 0

# NOTE this string will eventually contain the entire output FASTA file in
# memory; it'd be more efficient to split this into chunks to reduce space reqs
fasta_out = ""
with open(IN_FILENAME, "r") as gfa_file:
    for line in gfa_file:
        if line.startswith("S\t"):
            split = line.strip().split("\t")
            seq = split[2]
            fasta_out += ">{}\n".format(split[1])
            fasta_out += split[2] + "\n"
            num_seqs += 1

with open(OUT_FILENAME, "w") as fasta_file:
    fasta_file.write(fasta_out)

print(f"FASTA of {num_seqs} sequences created at {OUT_FILENAME}.")