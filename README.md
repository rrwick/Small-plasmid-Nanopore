<p align="center"><img src="banner.png" alt="Banner" width="100%"></p>

# Ligation vs rapid: recovery of small plasmid sequences from Oxford Nanopore sequencing data

This repository supplements our paper looking at small plasmid recovery from Oxford Nanopore sequencing:

[Wick RR, Judd LM, Wyres KL, Holt KE. Ligation vs rapid: recovery of small plasmid sequences from Oxford Nanopore sequencing data. bioRxiv. 2020; doi:TBA.](https://www.biorxiv.org/content/TBA).

<p align="center"><img src="banner.png" alt="Banner" width="100%"></p>



### Figures

The [`figures`](figures) directory contains all figures (both main-text and supplementary) for the study, in PDF and PNG formats.



### Method

The [`method.md`](method.md) file contains the commands I ran to conduct the analysis.



### Scripts

The [`scripts`](scripts) directory contains Python scripts I wrote for the analysis: `align_reads.py`, `assign_reads.py`, `get_depths.py`, `get_gc.py` and `depth_and_gc.py`. See the header in each script for more information on how it works, and see the [`method.md`](method.md) file for how I used these to produce the data in the study.



### Tables

The [`Table_S1.xlsx`](Table_S1.xlsx) file contains various stats at the run level, barcode level and replicon level. See the first worksheet in the file for a more detailed description of the content.



### Plots

The [`plots.Rmd`](plots.Rmd) file contains the R code used to generate plots for the figures.



### Data

The reads, assemblies and per-read tables are too large for GitHub, so you can download them from here:
[bridges.monash.edu/articles/dataset/Small_plasmid_Nanopore_data/13543754](https://bridges.monash.edu/articles/dataset/Small_plasmid_Nanopore_data/13543754)

There you will find these files:
* `tech_rep_1_ligation_reads.tar`: a FASTQ file and sequencing summary file for the first ligation run
* `tech_rep_1_rapid_reads.tar`: a FASTQ file and sequencing summary file for the first rapid run
* `tech_rep_2_ligation_reads.tar`: a FASTQ file and sequencing summary file for the second ligation run
* `tech_rep_2_rapid_reads.tar`: a FASTQ file and sequencing summary file for the second ligation run
* `assemblies.tar.gz`: reference assemblies for the seven isolates (FASTA format)
* `read_tables.tar`: the TSV output of `assign_reads.py` (one line per read) for each of the four sequencing runs
