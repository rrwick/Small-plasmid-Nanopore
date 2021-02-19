<p align="center"><img src="Fig_1_ligation_vs_rapid.png" alt="Figure 1" width="70%"></p>

**Figure 1**: conceptual illustration of Oxford Nanopore ligation and rapid sample preparation methods. When circular DNA is extracted from a bacterial cell (top-left), incidental fragmentation of the DNA occurs. The ligation preparation (bottom-left) comprises blunt-end ligation of barcodes/adapters onto DNA molecules, so circular pieces of DNA will not receive adapters and thus remain unavailable for sequencing. The rapid preparation (right) uses a transposome enzyme to add barcodes/adapters into the middle of DNA molecules, making both linear and circular DNA available for sequencing.

<br><br><br><br>




<p align="center"><img src="Fig_2_plasmid_abudance.png" alt="Figure 2" width="80%"></p>

**Figure 2**: plasmid abundance resulting from A) ligation and B) rapid ONT library preparation methods. Each point in the plots represents one plasmid. The read depth ratio is the normalised ONT read depth divided by the normalised Illumina read depth. The dashed lines at ratio=1 indicate perfect agreement of plasmid depths between ONT and Illumina data. Points above the dashed lines indicate plasmids that are overrepresented in ONT reads, while points below the dashed lines indicate plasmids that are underrepresented in ONT reads.

For ONT ligation reads (A), small plasmids are systematically underrepresented relative to Illumina reads. For ONT rapid reads (B), plasmid size has no clear effect, and depths for both small and large plasmids are in good agreement with Illumina reads.

<br><br><br><br>




<p align="center"><img src="Fig_S1_method.png" alt="Figure S1" width="80%"></p>

**Figure S1**: a diagrammatic representation of the study approach for the culturing, sequencing and assembly steps.

A. Seven bacterial isolates from seven different species: _A. baumannii_, _C. koseri_, _E. kobei_, _Haemophilus_ (unnamed species), _K. oxytoca_, _K. variicola_ and _S. marcescens_.

B. Each isolate was cultured and DNA was extracted in two separate technical replicates.

C. For each technical replicate, the DNA was multiplexed and sequenced using three different methods: ONT with a rapid preparation, ONT with a ligation preparation and Illumina.

D. Each ONT sequencing run produced a set of basecalled reads (pre-demultiplexing). These whole-run pooled reads were not available for the Illumina runs because they included isolates from other studies.

E. After demultiplexing, reads were available in per-genome files.

F. Genome assemblies were carried out using all available ONT and Illumina reads for each isolate. To account for the possibility of genomic differences between the two technical replicates, assemblies were performed on a per-replicate basis.

G. Assemblies for the two technical replicates were reconciled with each other to produce a single assembly for each isolate.

<br><br><br><br>




<p align="center"><img src="Fig_S2_genomes.png" alt="Figure S2" width="90%"></p>

**Figure S2**: reference genome assemblies for the seven isolates used in this study (replicon sizes not drawn to scale).

<br><br><br><br>




<p align="center"><img src="Fig_S3_illumina_gc.png" alt="Figure S3" width="80%"></p>

**Figure S3**: the association between GC content on Illumina read depth. Each green point represents a 1 kbp sequence window from the chromosome of a genome in this study, where read depth was normalised using the mean depth for 49–51% GC windows. The dark green line is a LOESS regression curve fitted to the points. The blue points on the top of the plot show the mean GC content of each plasmid in the study genomes.

<br><br><br><br>




<p align="center"><img src="Fig_S4_read_n50_by_barcode.png" alt="Figure S4" width="80%"></p>

**Figure S4**: the read N50 length for each demultiplexed read set in each of the four ONT sequencing runs.

<br><br><br><br>




<p align="center"><img src="Fig_S5_read_identity_distributions.png" alt="Figure S5" width="80%"></p>

**Figure S5**: read identity distributions for each of the four ONT sequencing runs. The dashed lines represent median read identity.

<br><br><br><br>




<p align="center"><img src="Fig_S6_translocation_speed_vs_time.png" alt="Figure S6" width="80%"></p>

**Figure S6**: pore translocation speed vs read time for the first 24 hours of each of the four ONT sequencing runs. Each dot represents a single read. The ligation 1 and rapid 1 runs were refueled with the EXP-FLP002 kit 18 hours into the run (dashed line).

<br><br><br><br>




<p align="center"><img src="Fig_S7_read_identity_vs_time.png" alt="Figure S7" width="80%"></p>

**Figure S7**: read identity vs read time for the first 24 hours of each of the four ONT sequencing runs. Each dot represents a single read. The ligation 1 and rapid 1 runs were refueled with the EXP-FLP002 kit 18 hours into the run (dashed line).
