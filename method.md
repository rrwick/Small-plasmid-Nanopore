# Reference genome assembly

## Prep files

I did this on my Nectar instance.

Make some directories:
```bash
mkdir ~/small_plasmids
mkdir ~/small_plasmids/tech_rep_1 ~/small_plasmids/tech_rep_2
mkdir ~/small_plasmids/tech_rep_1/rapid ~/small_plasmids/tech_rep_1/ligation ~/small_plasmids/tech_rep_1/pooled 
mkdir ~/small_plasmids/tech_rep_2/rapid ~/small_plasmids/tech_rep_2/ligation ~/small_plasmids/tech_rep_2/pooled
mkdir ~/small_plasmids/tech_rep_1/illumina ~/small_plasmids/tech_rep_2/illumina
mkdir ~/small_plasmids/tech_rep_1/illumina/barcode01 ~/small_plasmids/tech_rep_2/illumina/barcode01
mkdir ~/small_plasmids/tech_rep_1/illumina/barcode02 ~/small_plasmids/tech_rep_2/illumina/barcode02
mkdir ~/small_plasmids/tech_rep_1/illumina/barcode03 ~/small_plasmids/tech_rep_2/illumina/barcode03
mkdir ~/small_plasmids/tech_rep_1/illumina/barcode04 ~/small_plasmids/tech_rep_2/illumina/barcode04
mkdir ~/small_plasmids/tech_rep_1/illumina/barcode05 ~/small_plasmids/tech_rep_2/illumina/barcode05
mkdir ~/small_plasmids/tech_rep_1/illumina/barcode07 ~/small_plasmids/tech_rep_2/illumina/barcode07
mkdir ~/small_plasmids/tech_rep_1/illumina/barcode08 ~/small_plasmids/tech_rep_2/illumina/barcode08
```

Transfer Nanopore reads:
```bash
cd ~/small_plasmids/tech_rep_1/rapid
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/minion/2020-01-16_plasmid_rapid/fastq/barcode0*.fastq.gz" .
rm barcode06.fastq.gz barcode09.fastq.gz

cd ~/small_plasmids/tech_rep_1/ligation
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/minion/2020-01-16_plasmid_ligation/fastq/barcode0*.fastq.gz" .
rm barcode06.fastq.gz barcode09.fastq.gz

cd ~/small_plasmids/tech_rep_2/rapid
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/minion/2020-06-09_small_plasmid_rapid_02/fastq/barcode0*.fastq.gz" .
rm barcode06.fastq.gz barcode09.fastq.gz

cd ~/small_plasmids/tech_rep_2/ligation
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/minion/2020-06-10_small_plasmid_ligation_02/fastq/barcode0*.fastq.gz" .
rm barcode06.fastq.gz barcode09.fastq.gz
```

Transfer Illumina reads:
```bash
cd ~/small_plasmids/tech_rep_1/illumina/barcode01
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/other_illumina/NextSeq_ACBD_200217_Klebs_colistin_small_plasmids/FASTQ/plasmids-J9*.fastq.gz" .

cd ~/small_plasmids/tech_rep_1/illumina/barcode02
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/other_illumina/NextSeq_ACBD_200217_Klebs_colistin_small_plasmids/FASTQ/plasmids-MINF-9D*.fastq.gz" .

cd ~/small_plasmids/tech_rep_1/illumina/barcode03
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/other_illumina/NextSeq_ACBD_200217_Klebs_colistin_small_plasmids/FASTQ/plasmids-MSB1-1B*.fastq.gz" .

cd ~/small_plasmids/tech_rep_1/illumina/barcode04
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/other_illumina/NextSeq_ACBD_200217_Klebs_colistin_small_plasmids/FASTQ/plasmids-MIC132-1*.fastq.gz" .

cd ~/small_plasmids/tech_rep_1/illumina/barcode05
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/other_illumina/NextSeq_ACBD_200217_Klebs_colistin_small_plasmids/FASTQ/plasmids-MSB1-2C*.fastq.gz" .

cd ~/small_plasmids/tech_rep_1/illumina/barcode07
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/other_illumina/NextSeq_ACBD_200217_Klebs_colistin_small_plasmids/FASTQ/plasmids-INF345*.fastq.gz" .

cd ~/small_plasmids/tech_rep_1/illumina/barcode08
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/other_illumina/NextSeq_ACBD_200217_Klebs_colistin_small_plasmids/FASTQ/plasmids-17-147-1671*.fastq.gz" .

cd ~/small_plasmids/tech_rep_2/illumina/barcode01
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/other_illumina/NovaSeq_ACBD_200908_LJ_LB_small_plasmid/NovaSeq_ACBD_200908_LJ_LB_small_plasmid/20200908_wBF05_L001-ds.8b5f24e057d44075953a76c5cbac2914/*.fastq.gz" .

cd ~/small_plasmids/tech_rep_2/illumina/barcode02
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/other_illumina/NovaSeq_ACBD_200908_LJ_LB_small_plasmid/NovaSeq_ACBD_200908_LJ_LB_small_plasmid/20200908_wBG05_L001-ds.c1d86c48c6bc4367b2bf806e1bc820d4/*.fastq.gz" .

cd ~/small_plasmids/tech_rep_2/illumina/barcode03
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/other_illumina/NovaSeq_ACBD_200908_LJ_LB_small_plasmid/NovaSeq_ACBD_200908_LJ_LB_small_plasmid/20200908_wBH05_L001-ds.7d0983e737c8442da4440349c386ba77/*.fastq.gz" .

cd ~/small_plasmids/tech_rep_2/illumina/barcode04
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/other_illumina/NovaSeq_ACBD_200908_LJ_LB_small_plasmid/NovaSeq_ACBD_200908_LJ_LB_small_plasmid/20200908_wBA06_L001-ds.82f46b3ad89640c08ca3ed1707177ff8/*.fastq.gz" .

cd ~/small_plasmids/tech_rep_2/illumina/barcode05
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/other_illumina/NovaSeq_ACBD_200908_LJ_LB_small_plasmid/NovaSeq_ACBD_200908_LJ_LB_small_plasmid/20200908_wBB06_L001-ds.a1b1a2e6e4d448459ab3d9bac466563b/*.fastq.gz" .

cd ~/small_plasmids/tech_rep_2/illumina/barcode07
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/other_illumina/NovaSeq_ACBD_200908_LJ_LB_small_plasmid/NovaSeq_ACBD_200908_LJ_LB_small_plasmid/20200908_wBC06_L001-ds.827c833cd39440548620a3c69203b795/*.fastq.gz" .

cd ~/small_plasmids/tech_rep_2/illumina/barcode08
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/other_illumina/NovaSeq_ACBD_200908_LJ_LB_small_plasmid/NovaSeq_ACBD_200908_LJ_LB_small_plasmid/20200908_wBD06_L001-ds.d02a29bf341d4412b068392b8933c6e0/*.fastq.gz" .
```

Trim Illumina reads:
```bash
for d in ~/small_plasmids/tech_rep_1/illumina/barcode*; do
    cd "$d"
    fastp --in1 *_1.fastq.gz --in2 *_2.fastq.gz --out1 trimmed_1.fastq.gz --out2 trimmed_2.fastq.gz --unpaired1 trimmed_u.fastq.gz --unpaired2 trimmed_u.fastq.gz --trim_poly_g
done

for d in ~/small_plasmids/tech_rep_2/illumina/barcode*; do
    cd "$d"
    fastp --in1 *_R1_001.fastq.gz --in2 *_R2_001.fastq.gz --out1 trimmed_1.fastq.gz --out2 trimmed_2.fastq.gz --unpaired1 trimmed_u.fastq.gz --unpaired2 trimmed_u.fastq.gz --trim_poly_g
done
```

Unzip and pool reads:
```bash
cd ~/small_plasmids/tech_rep_1/pooled
for n in 1 2 3 4 5 7 8; do
    zcat ~/small_plasmids/tech_rep_1/rapid/barcode0"$n".fastq.gz > barcode0"$n".fastq
    zcat ~/small_plasmids/tech_rep_1/ligation/barcode0"$n".fastq.gz >> barcode0"$n".fastq
done

cd ~/small_plasmids/tech_rep_2/pooled
for n in 1 2 3 4 5 7 8; do
    zcat ~/small_plasmids/tech_rep_2/rapid/barcode0"$n".fastq.gz > barcode0"$n".fastq
    zcat ~/small_plasmids/tech_rep_2/ligation/barcode0"$n".fastq.gz >> barcode0"$n".fastq
done
```

These were the read sets after pooling:
```
filename                           seq_count  total_length   n99   n90    n50    n10    n01
tech_rep_1/pooled/barcode01.fastq     544069    2947202618   519  2371  14915  43166  73303
tech_rep_1/pooled/barcode02.fastq     341164    2102127159   518  3239  15176  43106  75058
tech_rep_1/pooled/barcode03.fastq     225234    1078337255   461  2045  14285  47724  85474
tech_rep_1/pooled/barcode04.fastq    2773242    4560929064   256   585   4203  21177  44642
tech_rep_1/pooled/barcode05.fastq     344520    1747148598   473  2399  12648  37673  64616
tech_rep_1/pooled/barcode07.fastq     248808    1481107440   574  2921  14048  43601  77274
tech_rep_1/pooled/barcode08.fastq    1770672    2160206027   211   395   4361  30546  67628
tech_rep_2/pooled/barcode01.fastq     187010    1850643051  1240  5383  18120  45254  71687
tech_rep_2/pooled/barcode02.fastq     353301    2675639125   782  4051  15590  41051  67847
tech_rep_2/pooled/barcode03.fastq     173222    1612872724  1308  5148  17745  42300  67051
tech_rep_2/pooled/barcode04.fastq     492127    3046365571   634  3284  11664  37071  64991
tech_rep_2/pooled/barcode05.fastq     141976    1292090692  1162  4731  17386  44740  72716
tech_rep_2/pooled/barcode07.fastq     300502    2450202793   658  4785  20349  49071  75569
tech_rep_2/pooled/barcode08.fastq     278032    1790818046   665  3060  15060  45573  73677
```

Clean up non-pooled files to save space:
```bash
rm -r ~/small_plasmids/tech_rep_*/rapid
rm -r ~/small_plasmids/tech_rep_*/ligation
```

I then ran Filtlong, first to clean up any short reads:
```bash
mkdir ~/small_plasmids/tech_rep_1/filtered_1
cd ~/small_plasmids/tech_rep_1/filtered_1
for n in 1 2 3 4 5 7 8; do
    filtlong --min_length 1000 ~/small_plasmids/tech_rep_1/pooled/barcode0"$n".fastq > barcode0"$n".fastq
done

mkdir ~/small_plasmids/tech_rep_2/filtered_1
cd ~/small_plasmids/tech_rep_2/filtered_1
for n in 1 2 3 4 5 7 8; do
    filtlong --min_length 1000 ~/small_plasmids/tech_rep_2/pooled/barcode0"$n".fastq > barcode0"$n".fastq
done
```

These were the read sets after filtering:
```
filename                               seq_count  total_length   n99   n90    n50    n10    n01
tech_rep_1/filtered_1/barcode01.fastq     368328    2848012195  1194  3060  15666  43676  73676
tech_rep_1/filtered_1/barcode02.fastq     232251    2047353348  1303  3919  15663  43584  75429
tech_rep_1/filtered_1/barcode03.fastq     140017    1032538203  1163  2812  15206  48583  86497
tech_rep_1/filtered_1/barcode04.fastq     959352    3665654045  1041  1482   6456  23811  47112
tech_rep_1/filtered_1/barcode05.fastq     229057    1687297544  1203  3103  13218  38143  64797
tech_rep_1/filtered_1/barcode07.fastq     178279    1442142805  1258  3470  14560  43992  77877
tech_rep_1/filtered_1/barcode08.fastq     338580    1552371524  1046  1622  11089  36742  72997
tech_rep_2/filtered_1/barcode01.fastq     159915    1837323088  1769  5606  18268  45354  71725
tech_rep_2/filtered_1/barcode02.fastq     277316    2636377452  1425  4448  15833  41275  67888
tech_rep_2/filtered_1/barcode03.fastq     143502    1602306661  1790  5353  17862  42384  67051
tech_rep_2/filtered_1/barcode04.fastq     370298    2982991520  1313  3750  12018  37353  65397
tech_rep_2/filtered_1/barcode05.fastq     120376    1282044734  1633  4964  17536  44839  72754
tech_rep_2/filtered_1/barcode07.fastq     210940    2406674303  1466  5450  20757  49296  75789
tech_rep_2/filtered_1/barcode08.fastq     210684    1756319661  1315  3511  15461  45843  73828
```

I then ran Filtlong, to clean up very low quality reads (thresholds based on eyeballing the distributions):
```bash
cd ~/small_plasmids
for f in */filtered_1/*.fastq; do
    seqtk sample $f 1000 >> random_sample.fastq
done
git clone https://github.com/rrwick/Filtlong
cd Filtlong
make -j
cd ..
Filtlong/scripts/read_info_histograms.sh random_sample.fastq
rm random_sample.fastq
rm -rf Filtlong

mkdir ~/small_plasmids/tech_rep_1/filtered_2
cd ~/small_plasmids/tech_rep_1/filtered_2
for n in 1 2 3 4 5 7 8; do
    filtlong --min_mean_q 80 --min_window_q 60 ~/small_plasmids/tech_rep_1/filtered_1/barcode0"$n".fastq > barcode0"$n".fastq
done

mkdir ~/small_plasmids/tech_rep_2/filtered_2
cd ~/small_plasmids/tech_rep_2/filtered_2
for n in 1 2 3 4 5 7 8; do
    filtlong --min_mean_q 80 --min_window_q 60 ~/small_plasmids/tech_rep_2/filtered_1/barcode0"$n".fastq > barcode0"$n".fastq
done
```

These were the read sets after filtering:
```
filename                               seq_count  total_length   n99   n90    n50    n10    n01
tech_rep_1/filtered_2/barcode01.fastq     359483  2756288556   1192  3034  15477  43240  72972
tech_rep_1/filtered_2/barcode02.fastq     225292  1962307477   1298  3872  15420  42677  73974
tech_rep_1/filtered_2/barcode03.fastq     136230   990994025   1160  2770  14896  47679  85409
tech_rep_1/filtered_2/barcode04.fastq     940358  3554517024   1040  1473   6329  23313  46111
tech_rep_1/filtered_2/barcode05.fastq     223173  1629234183   1200  3070  13057  37607  63863
tech_rep_1/filtered_2/barcode07.fastq     173427  1388044090   1253  3454  14350  43302  76648
tech_rep_1/filtered_2/barcode08.fastq     331447  1505165116   1045  1614  10878  35922  71121
tech_rep_2/filtered_2/barcode01.fastq     149855  1658753374   1713  5386  17540  44083  69306
tech_rep_2/filtered_2/barcode02.fastq     265870  2449635773   1403  4304  15251  39756  65991
tech_rep_2/filtered_2/barcode03.fastq     136435  1470675221   1744  5145  17181  41047  64355
tech_rep_2/filtered_2/barcode04.fastq     353418  2777160077   1299  3663  11534  35901  62187
tech_rep_2/filtered_2/barcode05.fastq     115029  1184128585   1596  4790  16844  43257  70459
tech_rep_2/filtered_2/barcode07.fastq     201104  2209585840   1437  5228  19810  47737  74256
tech_rep_2/filtered_2/barcode08.fastq     200375  1597897530   1297  3340  14584  43749  70294
```

Clean up intermediate files to save space:
```bash
rm -r ~/small_plasmids/tech_rep_*/pooled
rm -r ~/small_plasmids/tech_rep_*/filtered_1
```

I then subsampled each read set 15 times (5 assemblies each for Flye, Miniasm and Raven). The read counts were chosen to give about 50x depth each:
```bash
mkdir ~/small_plasmids/tech_rep_1/subsampled
mkdir ~/small_plasmids/tech_rep_2/subsampled

cd ~/small_plasmids/tech_rep_1/subsampled
for i in {00..14}; do
    seqtk sample -s "$i" ../filtered_2/barcode01.fastq 25757 > barcode01_sample_"$i".fastq
    seqtk sample -s "$i" ../filtered_2/barcode02.fastq 27744 > barcode02_sample_"$i".fastq
    seqtk sample -s "$i" ../filtered_2/barcode03.fastq 35009 > barcode03_sample_"$i".fastq
    seqtk sample -s "$i" ../filtered_2/barcode04.fastq 27937 > barcode04_sample_"$i".fastq
    seqtk sample -s "$i" ../filtered_2/barcode05.fastq 40995 > barcode05_sample_"$i".fastq
    seqtk sample -s "$i" ../filtered_2/barcode07.fastq 37188 > barcode07_sample_"$i".fastq
    seqtk sample -s "$i" ../filtered_2/barcode08.fastq 64981 > barcode08_sample_"$i".fastq
done

cd ~/small_plasmids/tech_rep_2/subsampled
for i in {00..14}; do
    seqtk sample -s "$i" ../filtered_2/barcode01.fastq 17841 > barcode01_sample_"$i".fastq
    seqtk sample -s "$i" ../filtered_2/barcode02.fastq 26228 > barcode02_sample_"$i".fastq
    seqtk sample -s "$i" ../filtered_2/barcode03.fastq 23626 > barcode03_sample_"$i".fastq
    seqtk sample -s "$i" ../filtered_2/barcode04.fastq 13438 > barcode04_sample_"$i".fastq
    seqtk sample -s "$i" ../filtered_2/barcode05.fastq 29072 > barcode05_sample_"$i".fastq
    seqtk sample -s "$i" ../filtered_2/barcode07.fastq 27089 > barcode07_sample_"$i".fastq
    seqtk sample -s "$i" ../filtered_2/barcode08.fastq 37004 > barcode08_sample_"$i".fastq
done
```




## Long-read assemblies

The input assemblies for Trycycler, using Flye v2.8, Miniasm/Minipolish v0.3/v0.1.3 and Raven v1.1.10:
```bash
mkdir ~/small_plasmids/tech_rep_1/assemblies
mkdir ~/small_plasmids/tech_rep_2/assemblies

for d in tech_rep_1 tech_rep_2; do
    cd ~/small_plasmids/"$d"/assemblies
    for b in 01 02 03 04 05 07 08; do
        flye --nano-raw ../subsampled/barcode"$b"_sample_00.fastq --threads 16 --plasmids --out-dir barcode"$b"_sample_00_flye; cp barcode"$b"_sample_00_flye/assembly.fasta barcode"$b"_sample_00_flye.fasta; rm -r barcode"$b"_sample_00_flye
        flye --nano-raw ../subsampled/barcode"$b"_sample_01.fastq --threads 16 --plasmids --out-dir barcode"$b"_sample_01_flye; cp barcode"$b"_sample_01_flye/assembly.fasta barcode"$b"_sample_01_flye.fasta; rm -r barcode"$b"_sample_01_flye
        flye --nano-raw ../subsampled/barcode"$b"_sample_02.fastq --threads 16 --plasmids --out-dir barcode"$b"_sample_02_flye; cp barcode"$b"_sample_02_flye/assembly.fasta barcode"$b"_sample_02_flye.fasta; rm -r barcode"$b"_sample_02_flye
        flye --nano-raw ../subsampled/barcode"$b"_sample_03.fastq --threads 16 --plasmids --out-dir barcode"$b"_sample_03_flye; cp barcode"$b"_sample_03_flye/assembly.fasta barcode"$b"_sample_03_flye.fasta; rm -r barcode"$b"_sample_03_flye
        flye --nano-raw ../subsampled/barcode"$b"_sample_04.fastq --threads 16 --plasmids --out-dir barcode"$b"_sample_04_flye; cp barcode"$b"_sample_04_flye/assembly.fasta barcode"$b"_sample_04_flye.fasta; rm -r barcode"$b"_sample_04_flye
    done
done

for d in tech_rep_1 tech_rep_2; do
    cd ~/small_plasmids/"$d"/assemblies
    for b in 01 02 03 04 05 07 08; do
        miniasm_and_minipolish.sh ../subsampled/barcode"$b"_sample_05.fastq 16 > barcode"$b"_sample_05_miniasm.gfa; any2fasta barcode"$b"_sample_05_miniasm.gfa > barcode"$b"_sample_05_miniasm.fasta; rm barcode"$b"_sample_05_miniasm.gfa
        miniasm_and_minipolish.sh ../subsampled/barcode"$b"_sample_06.fastq 16 > barcode"$b"_sample_06_miniasm.gfa; any2fasta barcode"$b"_sample_06_miniasm.gfa > barcode"$b"_sample_06_miniasm.fasta; rm barcode"$b"_sample_06_miniasm.gfa
        miniasm_and_minipolish.sh ../subsampled/barcode"$b"_sample_07.fastq 16 > barcode"$b"_sample_07_miniasm.gfa; any2fasta barcode"$b"_sample_07_miniasm.gfa > barcode"$b"_sample_07_miniasm.fasta; rm barcode"$b"_sample_07_miniasm.gfa
        miniasm_and_minipolish.sh ../subsampled/barcode"$b"_sample_08.fastq 16 > barcode"$b"_sample_08_miniasm.gfa; any2fasta barcode"$b"_sample_08_miniasm.gfa > barcode"$b"_sample_08_miniasm.fasta; rm barcode"$b"_sample_08_miniasm.gfa
        miniasm_and_minipolish.sh ../subsampled/barcode"$b"_sample_09.fastq 16 > barcode"$b"_sample_09_miniasm.gfa; any2fasta barcode"$b"_sample_09_miniasm.gfa > barcode"$b"_sample_09_miniasm.fasta; rm barcode"$b"_sample_09_miniasm.gfa
    done
done

for d in tech_rep_1 tech_rep_2; do
    cd ~/small_plasmids/"$d"/assemblies
    for b in 01 02 03 04 05 07 08; do
        raven --threads 16 ../subsampled/barcode"$b"_sample_10.fastq > barcode"$b"_sample_10_raven.fasta
        raven --threads 16 ../subsampled/barcode"$b"_sample_11.fastq > barcode"$b"_sample_11_raven.fasta
        raven --threads 16 ../subsampled/barcode"$b"_sample_12.fastq > barcode"$b"_sample_12_raven.fasta
        raven --threads 16 ../subsampled/barcode"$b"_sample_13.fastq > barcode"$b"_sample_13_raven.fasta
        raven --threads 16 ../subsampled/barcode"$b"_sample_14.fastq > barcode"$b"_sample_14_raven.fasta
    done
done
```

Clean up subsampled reads to save space:
```bash
rm -r ~/small_plasmids/tech_rep_*/subsampled
```

Trycycler clustering:
```bash
mkdir ~/small_plasmids/tech_rep_1/trycycler
mkdir ~/small_plasmids/tech_rep_2/trycycler

for d in tech_rep_1 tech_rep_2; do
    cd ~/small_plasmids/"$d"/
    for b in 01 02 03 04 05 07 08; do
        ~/Trycycler/trycycler-runner.py cluster --assemblies assemblies/barcode"$b"_*.fasta --reads filtered_2/barcode"$b".fastq --out_dir trycycler/barcode"$b" --threads 32 &> cluster.out
        mv cluster.out trycycler/barcode"$b"
    done
done
```

Manually pick clusters and make obvious sequence exclusions/repairs:
```bash
cd ~/small_plasmids/tech_rep_1/trycycler/barcode01
# kept all 3 clusters
# needed to repair the small plasmid in 3 out of the 5 Flye assemblies

cd ~/small_plasmids/tech_rep_1/trycycler/barcode02
# kept all 3 clusters
# needed to repair the small plasmid in 4 out of the 5 Flye assemblies

cd ~/small_plasmids/tech_rep_1/trycycler/barcode03
# kept the first 6 clusters - the others seemed to be botched/incomplete parts of plasmids:
mv cluster_007 bad_cluster_007
mv cluster_008 bad_cluster_008
mv cluster_009 bad_cluster_009
mv cluster_010 bad_cluster_010
mv cluster_011 bad_cluster_011
# some contigs looked not-so-great based on the tree, so I'll exclude some now:
mv cluster_001/1_contigs/O_Utg762.fasta cluster_001/1_contigs/O_Utg762.fasta.excluded
mv cluster_002/1_contigs/O_Utg760.fasta cluster_002/1_contigs/O_Utg760.fasta.excluded
mv cluster_002/1_contigs/N_Utg776.fasta cluster_002/1_contigs/N_Utg776.fasta.excluded
mv cluster_003/1_contigs/L_Utg764.fasta cluster_003/1_contigs/L_Utg764.fasta.excluded
mv cluster_006/1_contigs/H_utg000002c.fasta cluster_006/1_contigs/H_utg000002c.fasta.excluded
# needed to repair the small plasmid in the Flye assemblies of cluster 4 and the miniasm assemblies of cluster 5

cd ~/small_plasmids/tech_rep_1/trycycler/barcode04
# kept all 4 clusters
# needed to repair the plasmids in most Flye assemblies (and one miniasm assembly)

cd ~/small_plasmids/tech_rep_1/trycycler/barcode05
# there were two bad clusters (each with only a single contig):
mv cluster_005 bad_cluster_005
mv cluster_006 bad_cluster_006
# cluster 4 (small plasmid) was a bit messy, with 4 out of 5 Flye assemblies needing repair and a lot of redundant miniasm contigs (some of which I removed):
mv cluster_004/1_contigs/F_utg000004l.fasta cluster_004/1_contigs/F_utg000004l.fasta.excluded
mv cluster_004/1_contigs/F_utg000008l.fasta cluster_004/1_contigs/F_utg000008l.fasta.excluded
mv cluster_004/1_contigs/F_utg000014l.fasta cluster_004/1_contigs/F_utg000014l.fasta.excluded
mv cluster_004/1_contigs/G_utg000006l.fasta cluster_004/1_contigs/G_utg000006l.fasta.excluded
mv cluster_004/1_contigs/H_utg000002l.fasta cluster_004/1_contigs/H_utg000002l.fasta.excluded
mv cluster_004/1_contigs/H_utg000006l.fasta cluster_004/1_contigs/H_utg000006l.fasta.excluded
mv cluster_004/1_contigs/H_utg000008l.fasta cluster_004/1_contigs/H_utg000008l.fasta.excluded
mv cluster_004/1_contigs/H_utg000010l.fasta cluster_004/1_contigs/H_utg000010l.fasta.excluded
mv cluster_004/1_contigs/I_utg000007l.fasta cluster_004/1_contigs/I_utg000007l.fasta.excluded
mv cluster_004/1_contigs/I_utg000008l.fasta cluster_004/1_contigs/I_utg000008l.fasta.excluded
mv cluster_004/1_contigs/I_utg000012l.fasta cluster_004/1_contigs/I_utg000012l.fasta.excluded

cd ~/small_plasmids/tech_rep_1/trycycler/barcode07
# only the last cluster was bad (some artefact that occurred in Flye assemblies):
mv cluster_007 bad_cluster_007
# cluster 5 had a lot of redundant miniasm contigs (and also needed a lot of circularisation repair):
mv cluster_005/1_contigs/G_utg000006l.fasta cluster_005/1_contigs/G_utg000006l.fasta.excluded
mv cluster_005/1_contigs/G_utg000016l.fasta cluster_005/1_contigs/G_utg000016l.fasta.excluded
mv cluster_005/1_contigs/G_utg000020l.fasta cluster_005/1_contigs/G_utg000020l.fasta.excluded
mv cluster_005/1_contigs/G_utg000026l.fasta cluster_005/1_contigs/G_utg000026l.fasta.excluded
mv cluster_005/1_contigs/J_utg000003l.fasta cluster_005/1_contigs/J_utg000003l.fasta.excluded
mv cluster_005/1_contigs/J_utg000005l.fasta cluster_005/1_contigs/J_utg000005l.fasta.excluded
mv cluster_005/1_contigs/J_utg000008l.fasta cluster_005/1_contigs/J_utg000008l.fasta.excluded
mv cluster_005/1_contigs/J_utg000009l.fasta cluster_005/1_contigs/J_utg000009l.fasta.excluded 
mv cluster_005/1_contigs/I_utg000007l.fasta cluster_005/1_contigs/I_utg000007l.fasta.excluded
# cluster 6 also needed some circularisation repair

cd ~/small_plasmids/tech_rep_1/trycycler/barcode08
# this was definitely the worst one - lots of bad clusters:
mv cluster_002 bad_cluster_002
mv cluster_003 bad_cluster_003
mv cluster_006 bad_cluster_006
mv cluster_001/1_contigs/K_Utg1022.fasta cluster_001/1_contigs/K_Utg1022.fasta.excluded
mv cluster_008 bad_cluster_008
mv cluster_009 bad_cluster_009
mv cluster_011 bad_cluster_011
mv cluster_005/1_contigs/D_contig_2.fasta cluster_005/1_contigs/D_contig_2.fasta.excluded
mv cluster_005/1_contigs/A_contig_3.fasta cluster_005/1_contigs/A_contig_3.fasta.excluded
mv cluster_005/1_contigs/B_contig_12.fasta cluster_005/1_contigs/B_contig_12.fasta.excluded
mv cluster_005/1_contigs/C_contig_2.fasta cluster_005/1_contigs/C_contig_2.fasta.excluded
mv cluster_010 bad_cluster_010
mv cluster_012 bad_cluster_012
mv cluster_013 bad_cluster_013
mv cluster_014/1_contigs/F_utg000012c.fasta cluster_014/1_contigs/F_utg000012c.fasta.excluded
mv cluster_015 bad_cluster_015
mv cluster_016 bad_cluster_016
mv cluster_017 bad_cluster_017
mv cluster_018 bad_cluster_018
mv cluster_019 bad_cluster_019
mv cluster_020 bad_cluster_020
mv cluster_021 bad_cluster_021
mv cluster_022 bad_cluster_022
mv cluster_023 bad_cluster_023
mv cluster_024 bad_cluster_024
mv cluster_025 bad_cluster_025
mv cluster_026 bad_cluster_026
# cluster 7 was particularly difficult - I think there are multiple forms of this plasmid present
# I split this one into two different versions:
mkdir cluster_007_a cluster_007_b cluster_007_other
mkdir cluster_007_a/1_contigs cluster_007_b/1_contigs cluster_007_other/1_contigs
mv cluster_007/1_contigs/H_utg000004c.fasta cluster_007_a/1_contigs
mv cluster_007/1_contigs/F_utg000002l.fasta cluster_007_a/1_contigs
mv cluster_007/1_contigs/G_utg000001l.fasta cluster_007_a/1_contigs
mv cluster_007/1_contigs/G_utg000004l.fasta cluster_007_b/1_contigs
mv cluster_007/1_contigs/F_utg000006l.fasta cluster_007_b/1_contigs
mv cluster_007/1_contigs/F_utg000003l.fasta cluster_007_b/1_contigs
mv cluster_007/1_contigs/G_utg000008l.fasta cluster_007_b/1_contigs
mv cluster_007/1_contigs/J_utg000002c.fasta cluster_007_other/1_contigs
mv cluster_007/1_contigs/L_Utg1010.fasta cluster_007_other/1_contigs
mv cluster_007/1_contigs/G_utg000010l.fasta cluster_007_other/1_contigs
mv cluster_007/1_contigs/F_utg000007l.fasta cluster_007_other/1_contigs
mv cluster_007/1_contigs/L_Utg1004.fasta cluster_007_other/1_contigs
mv cluster_007/1_contigs/G_utg000002l.fasta cluster_007_other/1_contigs
mv cluster_007/1_contigs/I_utg000001c.fasta cluster_007_other/1_contigs
mv cluster_007/1_contigs/G_utg000011l.fasta cluster_007_other/1_contigs
rmdir cluster_007/1_contigs
rmdir cluster_007
mv cluster_007_other bad_cluster_007_other

cd ~/small_plasmids/tech_rep_2/trycycler/barcode01
# the large plasmid had a lot of incomplete contigs
mv cluster_002/1_contigs/C_contig_2.fasta cluster_002/1_contigs/C_contig_2.fasta.excluded
mv cluster_002/1_contigs/G_utg000002l.fasta cluster_002/1_contigs/G_utg000002l.fasta.excluded
mv cluster_002/1_contigs/H_utg000002l.fasta cluster_002/1_contigs/H_utg000002l.fasta.excluded
mv cluster_002/1_contigs/J_utg000002l.fasta cluster_002/1_contigs/J_utg000002l.fasta.excluded
mv cluster_002/1_contigs/N_Utg828.fasta cluster_002/1_contigs/N_Utg828.fasta.excluded
# the small plasmid was mostly good but needed some repair

cd ~/small_plasmids/tech_rep_2/trycycler/barcode02
mv cluster_004 bad_cluster_004
# some small plasmid repair

cd ~/small_plasmids/tech_rep_2/trycycler/barcode03
# small plasmids were a bit messy
mv cluster_007 bad_cluster_007
mv cluster_008 bad_cluster_008
mv cluster_009 bad_cluster_009
mv cluster_002/1_contigs/M_Utg1088.fasta cluster_002/1_contigs/M_Utg1088.fasta.excluded

cd ~/small_plasmids/tech_rep_2/trycycler/barcode04
mv cluster_005 bad_cluster_005
mv cluster_008 bad_cluster_008
mv cluster_009 bad_cluster_009
mv cluster_010 bad_cluster_010
mv cluster_011 bad_cluster_011
mv cluster_001/1_contigs/K_Utg786.fasta cluster_001/1_contigs/K_Utg786.fasta.excluded
mv cluster_001/1_contigs/M_Utg776.fasta cluster_001/1_contigs/M_Utg776.fasta.excluded
mv cluster_006/1_contigs/I_utg000007l.fasta cluster_006/1_contigs/I_utg000007l.fasta.excluded

cd ~/small_plasmids/tech_rep_2/trycycler/barcode05
# all clusters look good and no small plasmid repair needed

cd ~/small_plasmids/tech_rep_2/trycycler/barcode07
mv cluster_007 bad_cluster_007
mv cluster_003/1_contigs/M_Utg1182.fasta cluster_003/1_contigs/M_Utg1182.fasta.excluded

cd ~/small_plasmids/tech_rep_2/trycycler/barcode08
# this one was a mess (like in the first tech rep)
mv cluster_004 bad_cluster_004
mv cluster_008 bad_cluster_008
mv cluster_009 bad_cluster_009
mv cluster_012 bad_cluster_012
mv cluster_001/1_contigs/O_Utg1066.fasta cluster_001/1_contigs/O_Utg1066.fasta.excluded
mv cluster_002/1_contigs/M_Utg1144.fasta cluster_002/1_contigs/M_Utg1144.fasta.excluded
mv cluster_006 bad_cluster_006
mv cluster_010 bad_cluster_010
mv cluster_011 bad_cluster_011
mv cluster_003/1_contigs/L_Utg1132.fasta cluster_003/1_contigs/L_Utg1132.fasta.excluded
mv cluster_007 bad_cluster_007
mv cluster_013 bad_cluster_013
mv cluster_014 bad_cluster_014
mv cluster_015 bad_cluster_015
mv cluster_017 bad_cluster_017
mv cluster_018 bad_cluster_018
mv cluster_019 bad_cluster_019
mv cluster_020 bad_cluster_020
```

Trycycler reconcile, one cluster at a time:
```bash
cd ~/small_plasmids/tech_rep_1

~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode01.fastq --cluster_dir trycycler/barcode01/cluster_001
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode01.fastq --cluster_dir trycycler/barcode01/cluster_002
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode01.fastq --cluster_dir trycycler/barcode01/cluster_003

~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode02.fastq --cluster_dir trycycler/barcode02/cluster_001
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode02.fastq --cluster_dir trycycler/barcode02/cluster_002
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode02.fastq --cluster_dir trycycler/barcode02/cluster_003

~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode03.fastq --cluster_dir trycycler/barcode03/cluster_001
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode03.fastq --cluster_dir trycycler/barcode03/cluster_002
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode03.fastq --cluster_dir trycycler/barcode03/cluster_003
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode03.fastq --cluster_dir trycycler/barcode03/cluster_004
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode03.fastq --cluster_dir trycycler/barcode03/cluster_005
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode03.fastq --cluster_dir trycycler/barcode03/cluster_006

~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode04.fastq --cluster_dir trycycler/barcode04/cluster_001
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode04.fastq --cluster_dir trycycler/barcode04/cluster_002
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode04.fastq --cluster_dir trycycler/barcode04/cluster_003
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode04.fastq --cluster_dir trycycler/barcode04/cluster_004

~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode05.fastq --cluster_dir trycycler/barcode05/cluster_001
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode05.fastq --cluster_dir trycycler/barcode05/cluster_002
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode05.fastq --cluster_dir trycycler/barcode05/cluster_003
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode05.fastq --cluster_dir trycycler/barcode05/cluster_004

~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode07.fastq --cluster_dir trycycler/barcode07/cluster_001
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode07.fastq --cluster_dir trycycler/barcode07/cluster_002
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode07.fastq --cluster_dir trycycler/barcode07/cluster_003
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode07.fastq --cluster_dir trycycler/barcode07/cluster_004 --linear
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode07.fastq --cluster_dir trycycler/barcode07/cluster_005
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode07.fastq --cluster_dir trycycler/barcode07/cluster_006

~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode08.fastq --cluster_dir trycycler/barcode08/cluster_001
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode08.fastq --cluster_dir trycycler/barcode08/cluster_004
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode08.fastq --cluster_dir trycycler/barcode08/cluster_005
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode08.fastq --cluster_dir trycycler/barcode08/cluster_007_a
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode08.fastq --cluster_dir trycycler/barcode08/cluster_007_b
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode08.fastq --cluster_dir trycycler/barcode08/cluster_014

cd ~/small_plasmids/tech_rep_2

~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode01.fastq --cluster_dir trycycler/barcode01/cluster_001
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode01.fastq --cluster_dir trycycler/barcode01/cluster_002
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode01.fastq --cluster_dir trycycler/barcode01/cluster_003

~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode02.fastq --cluster_dir trycycler/barcode02/cluster_001
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode02.fastq --cluster_dir trycycler/barcode02/cluster_002
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode02.fastq --cluster_dir trycycler/barcode02/cluster_003

~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode03.fastq --cluster_dir trycycler/barcode03/cluster_001
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode03.fastq --cluster_dir trycycler/barcode03/cluster_002
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode03.fastq --cluster_dir trycycler/barcode03/cluster_003
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode03.fastq --cluster_dir trycycler/barcode03/cluster_004
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode03.fastq --cluster_dir trycycler/barcode03/cluster_005
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode03.fastq --cluster_dir trycycler/barcode03/cluster_006

~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode04.fastq --cluster_dir trycycler/barcode04/cluster_001
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode04.fastq --cluster_dir trycycler/barcode04/cluster_002
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode04.fastq --cluster_dir trycycler/barcode04/cluster_003
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode04.fastq --cluster_dir trycycler/barcode04/cluster_004
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode04.fastq --cluster_dir trycycler/barcode04/cluster_006
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode04.fastq --cluster_dir trycycler/barcode04/cluster_007

~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode05.fastq --cluster_dir trycycler/barcode05/cluster_001
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode05.fastq --cluster_dir trycycler/barcode05/cluster_002
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode05.fastq --cluster_dir trycycler/barcode05/cluster_003
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode05.fastq --cluster_dir trycycler/barcode05/cluster_004
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode05.fastq --cluster_dir trycycler/barcode05/cluster_005

~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode07.fastq --cluster_dir trycycler/barcode07/cluster_001
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode07.fastq --cluster_dir trycycler/barcode07/cluster_002
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode07.fastq --cluster_dir trycycler/barcode07/cluster_003
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode07.fastq --cluster_dir trycycler/barcode07/cluster_004 --linear
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode07.fastq --cluster_dir trycycler/barcode07/cluster_005
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode07.fastq --cluster_dir trycycler/barcode07/cluster_006

~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode08.fastq --cluster_dir trycycler/barcode08/cluster_001
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode08.fastq --cluster_dir trycycler/barcode08/cluster_002
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode08.fastq --cluster_dir trycycler/barcode08/cluster_003
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode08.fastq --cluster_dir trycycler/barcode08/cluster_005_a
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode08.fastq --cluster_dir trycycler/barcode08/cluster_005_b
~/Trycycler/trycycler-runner.py reconcile --reads filtered_2/barcode08.fastq --cluster_dir trycycler/barcode08/cluster_016
```

Trycycler MSA:
```bash
cd ~/small_plasmids/tech_rep_1
for d in trycycler/barcode0*/cluster_*; do
    ~/Trycycler/trycycler-runner.py msa --cluster_dir "$d" --threads 32
done

cd ~/small_plasmids/tech_rep_2
for d in trycycler/barcode0*/cluster_*; do
    ~/Trycycler/trycycler-runner.py msa --cluster_dir "$d" --threads 32
done
```

Trycycler partition:
```bash
cd ~/small_plasmids/tech_rep_1
for b in 01 02 03 04 05 07 08; do
    ~/Trycycler/trycycler-runner.py partition --reads filtered_2/barcode"$b".fastq --cluster_dirs trycycler/barcode"$b"/cluster_* --threads 32
done

cd ~/small_plasmids/tech_rep_2
for b in 01 02 03 04 05 07 08; do
    ~/Trycycler/trycycler-runner.py partition --reads filtered_2/barcode"$b".fastq --cluster_dirs trycycler/barcode"$b"/cluster_* --threads 32
done
```

Trycycler consensus:
```bash
cd ~/small_plasmids/tech_rep_1
for d in trycycler/barcode0*/cluster_*; do
    ~/Trycycler/trycycler-runner.py consensus --cluster_dir "$d" --threads 32
done

cd ~/small_plasmids/tech_rep_2
for d in trycycler/barcode0*/cluster_*; do
    ~/Trycycler/trycycler-runner.py consensus --cluster_dir "$d" --threads 32
done
```

Medaka:
```bash
# Need to first activate conda by running the chunk in my .bashrc file.
conda activate medaka

for d in ~/small_plasmids/tech_rep_*/trycycler/barcode0*/cluster_*; do
    cd "$d"
    medaka_consensus -i 4_reads.fastq -d 7_final_consensus.fasta -o medaka -m r941_min_high_g360 -t 32
    mv medaka/consensus.fasta 8_medaka.fasta
    rm -r medaka *.fai *.mmi
done
```

Combine contigs to make final Nanopore-only Trycycler assemblies:
```bash
cd ~/small_plasmids/tech_rep_1/trycycler

echo ">chromosome" > barcode01.fasta; tail -n1 barcode01/cluster_001/8_medaka.fasta >> barcode01.fasta
echo ">plasmid_1" >> barcode01.fasta; tail -n1 barcode01/cluster_002/8_medaka.fasta >> barcode01.fasta
echo ">plasmid_2" >> barcode01.fasta; tail -n1 barcode01/cluster_003/8_medaka.fasta >> barcode01.fasta

echo ">chromosome" > barcode02.fasta; tail -n1 barcode02/cluster_001/8_medaka.fasta >> barcode02.fasta
echo ">plasmid_1" >> barcode02.fasta; tail -n1 barcode02/cluster_002/8_medaka.fasta >> barcode02.fasta
echo ">plasmid_2" >> barcode02.fasta; tail -n1 barcode02/cluster_003/8_medaka.fasta >> barcode02.fasta

echo ">chromosome" > barcode03.fasta; tail -n1 barcode03/cluster_001/8_medaka.fasta >> barcode03.fasta
echo ">plasmid_1" >> barcode03.fasta; tail -n1 barcode03/cluster_002/8_medaka.fasta >> barcode03.fasta
echo ">plasmid_2" >> barcode03.fasta; tail -n1 barcode03/cluster_003/8_medaka.fasta >> barcode03.fasta
echo ">plasmid_3" >> barcode03.fasta; tail -n1 barcode03/cluster_004/8_medaka.fasta >> barcode03.fasta
echo ">plasmid_4" >> barcode03.fasta; tail -n1 barcode03/cluster_006/8_medaka.fasta >> barcode03.fasta
echo ">plasmid_5" >> barcode03.fasta; tail -n1 barcode03/cluster_005/8_medaka.fasta >> barcode03.fasta

echo ">chromosome" > barcode04.fasta; tail -n1 barcode04/cluster_001/8_medaka.fasta >> barcode04.fasta
echo ">plasmid_1" >> barcode04.fasta; tail -n1 barcode04/cluster_002/8_medaka.fasta >> barcode04.fasta
echo ">plasmid_2" >> barcode04.fasta; tail -n1 barcode04/cluster_003/8_medaka.fasta >> barcode04.fasta
echo ">plasmid_3" >> barcode04.fasta; tail -n1 barcode04/cluster_004/8_medaka.fasta >> barcode04.fasta

echo ">chromosome" > barcode05.fasta; tail -n1 barcode05/cluster_001/8_medaka.fasta >> barcode05.fasta
echo ">plasmid_1" >> barcode05.fasta; tail -n1 barcode05/cluster_002/8_medaka.fasta >> barcode05.fasta
echo ">plasmid_2" >> barcode05.fasta; tail -n1 barcode05/cluster_003/8_medaka.fasta >> barcode05.fasta
echo ">plasmid_3" >> barcode05.fasta; tail -n1 barcode05/cluster_004/8_medaka.fasta >> barcode05.fasta

echo ">chromosome" > barcode07.fasta; tail -n1 barcode07/cluster_001/8_medaka.fasta >> barcode07.fasta
echo ">plasmid_1" >> barcode07.fasta; tail -n1 barcode07/cluster_002/8_medaka.fasta >> barcode07.fasta
echo ">plasmid_2" >> barcode07.fasta; tail -n1 barcode07/cluster_003/8_medaka.fasta >> barcode07.fasta
echo ">plasmid_3" >> barcode07.fasta; tail -n1 barcode07/cluster_004/8_medaka.fasta >> barcode07.fasta
echo ">plasmid_4" >> barcode07.fasta; tail -n1 barcode07/cluster_005/8_medaka.fasta >> barcode07.fasta
echo ">plasmid_5" >> barcode07.fasta; tail -n1 barcode07/cluster_006/8_medaka.fasta >> barcode07.fasta

echo ">chromosome" > barcode08.fasta; tail -n1 barcode08/cluster_001/8_medaka.fasta >> barcode08.fasta
echo ">plasmid_1" >> barcode08.fasta; tail -n1 barcode08/cluster_005/8_medaka.fasta >> barcode08.fasta
echo ">plasmid_2" >> barcode08.fasta; tail -n1 barcode08/cluster_004/8_medaka.fasta >> barcode08.fasta
echo ">plasmid_3" >> barcode08.fasta; tail -n1 barcode08/cluster_007_a/8_medaka.fasta >> barcode08.fasta
echo ">plasmid_4" >> barcode08.fasta; tail -n1 barcode08/cluster_014/8_medaka.fasta >> barcode08.fasta

cd ~/small_plasmids/tech_rep_2/trycycler

echo ">chromosome" > barcode01.fasta; tail -n1 barcode01/cluster_001/8_medaka.fasta >> barcode01.fasta
echo ">plasmid_1" >> barcode01.fasta; tail -n1 barcode01/cluster_002/8_medaka.fasta >> barcode01.fasta
echo ">plasmid_2" >> barcode01.fasta; tail -n1 barcode01/cluster_003/8_medaka.fasta >> barcode01.fasta

echo ">chromosome" > barcode02.fasta; tail -n1 barcode02/cluster_001/8_medaka.fasta >> barcode02.fasta
echo ">plasmid_1" >> barcode02.fasta; tail -n1 barcode02/cluster_002/8_medaka.fasta >> barcode02.fasta
echo ">plasmid_2" >> barcode02.fasta; tail -n1 barcode02/cluster_003/8_medaka.fasta >> barcode02.fasta

echo ">chromosome" > barcode03.fasta; tail -n1 barcode03/cluster_001/8_medaka.fasta >> barcode03.fasta
echo ">plasmid_1" >> barcode03.fasta; tail -n1 barcode03/cluster_002/8_medaka.fasta >> barcode03.fasta
echo ">plasmid_2" >> barcode03.fasta; tail -n1 barcode03/cluster_003/8_medaka.fasta >> barcode03.fasta
echo ">plasmid_3" >> barcode03.fasta; tail -n1 barcode03/cluster_005/8_medaka.fasta >> barcode03.fasta
echo ">plasmid_4" >> barcode03.fasta; tail -n1 barcode03/cluster_004/8_medaka.fasta >> barcode03.fasta
echo ">plasmid_5" >> barcode03.fasta; tail -n1 barcode03/cluster_006/8_medaka.fasta >> barcode03.fasta

echo ">chromosome" > barcode04.fasta; tail -n1 barcode04/cluster_001/8_medaka.fasta >> barcode04.fasta
echo ">plasmid_1" >> barcode04.fasta; tail -n1 barcode04/cluster_002/8_medaka.fasta >> barcode04.fasta
echo ">plasmid_2" >> barcode04.fasta; tail -n1 barcode04/cluster_003/8_medaka.fasta >> barcode04.fasta
echo ">plasmid_3" >> barcode04.fasta; tail -n1 barcode04/cluster_004/8_medaka.fasta >> barcode04.fasta
echo ">plasmid_4" >> barcode04.fasta; tail -n1 barcode04/cluster_006/8_medaka.fasta >> barcode04.fasta
echo ">plasmid_5" >> barcode04.fasta; tail -n1 barcode04/cluster_007/8_medaka.fasta >> barcode04.fasta

echo ">chromosome" > barcode05.fasta; tail -n1 barcode05/cluster_001/8_medaka.fasta >> barcode05.fasta
echo ">plasmid_1" >> barcode05.fasta; tail -n1 barcode05/cluster_002/8_medaka.fasta >> barcode05.fasta
echo ">plasmid_2" >> barcode05.fasta; tail -n1 barcode05/cluster_003/8_medaka.fasta >> barcode05.fasta
echo ">plasmid_3" >> barcode05.fasta; tail -n1 barcode05/cluster_004/8_medaka.fasta >> barcode05.fasta
echo ">plasmid_4" >> barcode05.fasta; tail -n1 barcode05/cluster_005/8_medaka.fasta >> barcode05.fasta

echo ">chromosome" > barcode07.fasta; tail -n1 barcode07/cluster_001/8_medaka.fasta >> barcode07.fasta
echo ">plasmid_1" >> barcode07.fasta; tail -n1 barcode07/cluster_002/8_medaka.fasta >> barcode07.fasta
echo ">plasmid_2" >> barcode07.fasta; tail -n1 barcode07/cluster_003/8_medaka.fasta >> barcode07.fasta
echo ">plasmid_3" >> barcode07.fasta; tail -n1 barcode07/cluster_004/8_medaka.fasta >> barcode07.fasta
echo ">plasmid_4" >> barcode07.fasta; tail -n1 barcode07/cluster_005/8_medaka.fasta >> barcode07.fasta
echo ">plasmid_5" >> barcode07.fasta; tail -n1 barcode07/cluster_006/8_medaka.fasta >> barcode07.fasta

echo ">chromosome" > barcode08.fasta; tail -n1 barcode08/cluster_001/8_medaka.fasta >> barcode08.fasta
echo ">plasmid_1" >> barcode08.fasta; tail -n1 barcode08/cluster_003/8_medaka.fasta >> barcode08.fasta
echo ">plasmid_2" >> barcode08.fasta; tail -n1 barcode08/cluster_002/8_medaka.fasta >> barcode08.fasta
echo ">plasmid_3" >> barcode08.fasta; tail -n1 barcode08/cluster_005_a/8_medaka.fasta >> barcode08.fasta
echo ">plasmid_4" >> barcode08.fasta; tail -n1 barcode08/cluster_016/8_medaka.fasta >> barcode08.fasta
```

Clean up:
```bash
rm -r /home/ubuntu/small_plasmids/tech_rep_*/assemblies
```

Unicycler Illumina-only:
```bash
mkdir ~/small_plasmids/tech_rep_1/unicycler
mkdir ~/small_plasmids/tech_rep_2/unicycler

for d in tech_rep_1 tech_rep_2; do
    cd ~/small_plasmids/"$d"
    for b in 01 02 03 04 05 07 08; do
        mkdir unicycler/barcode"$b"
        unicycler -1 illumina/barcode"$b"/trimmed_1.fastq.gz -2 illumina/barcode"$b"/trimmed_2.fastq.gz -s illumina/barcode"$b"/trimmed_u.fastq.gz -o unicycler/barcode"$b"/01_illumina_only --no_correct --no_pilon --threads 32
    done
done
```

At this point I didn't like the arrangement of the data, so I moved things around a bit:
```bash
for d in tech_rep_1 tech_rep_2; do
    for b in 01 02 03 04 05 07 08; do
        mkdir ~/small_plasmids/"$d"_barcode"$b"
        mv /home/ubuntu/small_plasmids/"$d"/illumina/barcode"$b" ~/small_plasmids/"$d"_barcode"$b"/illumina_reads
        mkdir ~/small_plasmids/"$d"_barcode"$b"/illumina_reads
        mkdir ~/small_plasmids/"$d"_barcode"$b"/nanopore_reads
        mv ~/small_plasmids/"$d"/filtered_2/barcode"$b".fastq ~/small_plasmids/"$d"_barcode"$b"/nanopore_reads/filtered.fastq
        mv ~/small_plasmids/"$d"/trycycler/barcode"$b" ~/small_plasmids/"$d"_barcode"$b"/trycycler
        mv ~/small_plasmids/"$d"/trycycler/barcode"$b".fasta ~/small_plasmids/"$d"_barcode"$b"/trycycler/assembly.fasta
        mkdir ~/small_plasmids/"$d"_barcode"$b"/unicycler
        mv ~/small_plasmids/"$d"/unicycler/barcode"$b"/01_illumina_only ~/small_plasmids/"$d"_barcode"$b"/unicycler/01_illumina_only
    done
done
rmdir ~/small_plasmids/tech_rep_[12]/*
rmdir ~/small_plasmids/tech_rep_[12]
```



















## Polishing

This was done for each replicate/barcode:
```bash
cd ~/small_plasmids/tech_rep_1_barcode01/trycycler
```

First, set some variables to make it easier:
```bash
illumina_1=../illumina_reads/trimmed_1.fastq.gz
illumina_2=../illumina_reads/trimmed_2.fastq.gz
illumina_u=../illumina_reads/trimmed_u.fastq.gz
nanopore=../nanopore_reads/filtered.fastq
threads=32
```

Initial alignment for insert size range:
```bash
bowtie2-build assembly.fasta assembly.fasta &> /dev/null
bowtie2 -1 "$illumina_1" -2 "$illumina_2" -x assembly.fasta --fast --threads "$threads" -I 0 -X 1000 -S insert_size_test.sam
```

Run this Python code to find the insert size range (can do this before Bowtie2 finishes):
```python
import math

def get_percentile(sorted_list, percentile):
    if not sorted_list:
        return 0.0
    fraction = percentile / 100.0
    rank = int(math.ceil(fraction * len(sorted_list)))
    if rank == 0:
        return sorted_list[0]
    return sorted_list[rank - 1]

insert_sizes = []
with open('insert_size_test.sam', 'rt') as raw_sam:
    for sam_line in raw_sam:
        try:
            sam_parts = sam_line.split('\t')
            sam_flags = int(sam_parts[1])
            if sam_flags & 2:  # if read mapped in proper pair
                insert_size = int(sam_parts[8])
                if insert_size > 0.0:
                    insert_sizes.append(insert_size)
        except (ValueError, IndexError):
            pass

insert_sizes = sorted(insert_sizes)
insert_size_1st = get_percentile(insert_sizes, 1.0)
insert_size_99th = get_percentile(insert_sizes, 99.0)
print(len(insert_sizes))
print(insert_size_1st, insert_size_99th)
```

Insert size results:
* tech_rep_1_barcode01: 157-699 (99.58% overall alignment rate)
* tech_rep_1_barcode02: 159-721 (99.45% overall alignment rate)
* tech_rep_1_barcode03: 160-717 (99.00% overall alignment rate)
* tech_rep_1_barcode04: 160-739 (98.54% overall alignment rate)
* tech_rep_1_barcode05: 157-715 (97.03% overall alignment rate)
* tech_rep_1_barcode07: 156-702 (99.22% overall alignment rate)
* tech_rep_1_barcode08: 159-705 (98.46% overall alignment rate)
* tech_rep_2_barcode01: 155-677 (98.20% overall alignment rate)
* tech_rep_2_barcode02: 155-738 (93.79% overall alignment rate)
* tech_rep_2_barcode03: 156-764 (98.83% overall alignment rate)
* tech_rep_2_barcode04: 155-743 (86.67% overall alignment rate)
* tech_rep_2_barcode05: 154-707 (97.29% overall alignment rate)
* tech_rep_2_barcode07: 155-673 (99.43% overall alignment rate)
* tech_rep_2_barcode08: 155-721 (97.84% overall alignment rate)

```bash
rm *.bt2 insert_size_test.sam
```

Pilon polishing:
```bash
insert_min=155
insert_max=721

before=assembly
after=round_1
bowtie2-build "$before".fasta "$before".fasta &> /dev/null
bowtie2 -1 "$illumina_1" -2 "$illumina_2" -x "$before".fasta --threads "$threads" -I "$insert_min" -X "$insert_max" --local --very-sensitive-local | samtools sort > illumina_alignments.bam
bowtie2 -U "$illumina_u" -x "$before".fasta --threads "$threads" --local --very-sensitive-local | samtools sort > illumina_alignments_u.bam
samtools index illumina_alignments.bam
samtools index illumina_alignments_u.bam
pilon --genome "$before".fasta --frags illumina_alignments.bam --unpaired illumina_alignments_u.bam --output "$after" --changes
rm *.bam *.bam.bai *.bt2
sed -i 's/_pilon//' "$after".fasta

before=round_1
after=round_2
bowtie2-build "$before".fasta "$before".fasta &> /dev/null
bowtie2 -1 "$illumina_1" -2 "$illumina_2" -x "$before".fasta --threads "$threads" -I "$insert_min" -X "$insert_max" --local --very-sensitive-local | samtools sort > illumina_alignments.bam
bowtie2 -U "$illumina_u" -x "$before".fasta --threads "$threads" --local --very-sensitive-local | samtools sort > illumina_alignments_u.bam
samtools index illumina_alignments.bam
samtools index illumina_alignments_u.bam
pilon --genome "$before".fasta --frags illumina_alignments.bam --unpaired illumina_alignments_u.bam --output "$after" --changes
rm *.bam *.bam.bai *.bt2
sed -i 's/_pilon//' "$after".fasta

before=round_2
after=round_3
bowtie2-build "$before".fasta "$before".fasta &> /dev/null
bowtie2 -1 "$illumina_1" -2 "$illumina_2" -x "$before".fasta --threads "$threads" -I "$insert_min" -X "$insert_max" --local --very-sensitive-local | samtools sort > illumina_alignments.bam
bowtie2 -U "$illumina_u" -x "$before".fasta --threads "$threads" --local --very-sensitive-local | samtools sort > illumina_alignments_u.bam
samtools index illumina_alignments.bam
samtools index illumina_alignments_u.bam
pilon --genome "$before".fasta --frags illumina_alignments.bam --unpaired illumina_alignments_u.bam --output "$after" --changes
rm *.bam *.bam.bai *.bt2
sed -i 's/_pilon//' "$after".fasta

before=round_3
after=round_4
bowtie2-build "$before".fasta "$before".fasta &> /dev/null
bowtie2 -1 "$illumina_1" -2 "$illumina_2" -x "$before".fasta --threads "$threads" -I "$insert_min" -X "$insert_max" --local --very-sensitive-local | samtools sort > illumina_alignments.bam
bowtie2 -U "$illumina_u" -x "$before".fasta --threads "$threads" --local --very-sensitive-local | samtools sort > illumina_alignments_u.bam
samtools index illumina_alignments.bam
samtools index illumina_alignments_u.bam
pilon --genome "$before".fasta --frags illumina_alignments.bam --unpaired illumina_alignments_u.bam --output "$after" --changes
rm *.bam *.bam.bai *.bt2
sed -i 's/_pilon//' "$after".fasta

before=round_4
after=round_5
bowtie2-build "$before".fasta "$before".fasta &> /dev/null
bowtie2 -1 "$illumina_1" -2 "$illumina_2" -x "$before".fasta --threads "$threads" -I "$insert_min" -X "$insert_max" --local --very-sensitive-local | samtools sort > illumina_alignments.bam
bowtie2 -U "$illumina_u" -x "$before".fasta --threads "$threads" --local --very-sensitive-local | samtools sort > illumina_alignments_u.bam
samtools index illumina_alignments.bam
samtools index illumina_alignments_u.bam
pilon --genome "$before".fasta --frags illumina_alignments.bam --unpaired illumina_alignments_u.bam --output "$after" --changes
rm *.bam *.bam.bai *.bt2
sed -i 's/_pilon//' "$after".fasta
```
When a Pilon round made no changes, I stopped.

Rename the final one:
```bash
final_round=$(ls round*.fasta | tail -n1)
mv $final_round polished.fasta
rm round*.fasta
seqtk seq polished.fasta > temp.fasta; mv temp.fasta polished.fasta  # remove newlines
```






## Finalising

I then manually finalised each of the assemblies by:
* comparing the tech rep 1 and 2 sequences together and investigating any differences
* ensuring that small plasmid sequences exactly match the Illumina graph

Barcode 1 needed no changes (the tech reps gave identical sequences).

Barcode 2 just needed three homopolymers fixed up:
* two in the big 29 kbp repeat
* one in a non-repetitive sequence

Barcode 3 needed no changes. There was a 1 bp difference in the smallest plasmid, but this was reflected in the Illumina graph so I think it's genuine.

Barcode 4 was a tricky one!
* The 39 kbp plasmids had a big disagreement:
  * Rep 1 Trycycler+Pilon was 39398 bp.
  * Rep 2 Trycycler+Pilon was 39345 bp.
  * They were about the same pre-Pilon and closer to rep 1. I.e. Pilon removed ~50 bp in rep 2.
  * The part in question has very low GC content and was a bit repetitive.
  * The Illumina graphs support the shorter sequence in rep 2 - they assembled completely.
  * However, when I aligned the long reads to both options, both rep 1 and rep 2 support the longer sequence!
  * I therefore conclude:
    * The longer sequence (39398 bp) is correct and changed rep 2 accordingly.
    * Illumina coverage sucked over that region (due to low GC) which is why the Illumina graphs (and in one case Pilon) preferred the shorter sequence.
* The chromosome had a discrepancy in a repetitve region:
  * It occurred in a 3x repeat (maybe rRNA)
  * Two variants differing by 1 bp: short (TGAGTGAAGC) and long (TGAGTGGAAGC).
  * Each of the technical replicates had one instance of the long variant, but in different positions.
  * The Illumina graph only had the short variant.
  * I aligned the Nanopore reads, and they always seem to prefer the short variant.
  * I therefore concluded that the short variant is the real one and the long variant was maybe a Medaka error that couldn't be Pilon-fixed because it was in a repeat.

Barcode 5:
* The second-largest plasmid (58 kbp):
  * Was in exact agreement between the two Trycycler+Pilon assemblies: 58,472 bp
  * However, the Illumina graphs were more ambiguous:
    * The first run had the plasmid at 58,382 bp.
    * The second run had a loop in the plasmid, one instance giving 58,382 bp and two instances giving 58,472 bp.
    * The repeat section was pretty high GC (73%)
  * I'm therefore believing the Trycycler+Pilon assemblies and leaving it at 58,472 bp.
* The chromosome had a small (1 bp) difference in a repeat:
    * The Illumina graphs only supported the longer option.
    * Each Trycycler+Pilon assembly had a copy of the longer option.
    * I therefore concluded that the longer option was the correct one and Pilon couldn't fix it because it was in a repeat.

Barcode 7:
* The two small plasmids were identical and in agreement with the Illumina graph, so I left them alone.
* The two large plasmids were also identical and in agreement with the Illumina graph (as far as I could tell), so I left them alone too.
* The linear plasmid was mostly in agreement, except for a few bases at the end, which I fixed up to be the same between the two.
* The chromosome had a big discrepancy:
  * Rep 1 was missing 221 bases compared to rep 2.
  * Rep 1's Illumina assembly graph broke at this point, so I think coverage was poor there.
  * The genomes were in agreement pre-Pilon, i.e. it was Pilon that made the deletion.
  * I therefore think the longer version is correct and changes rep 1 accordingly.

Barcode 8:
* Three of the plasmids were an exact match and I left them alone.
* The 161 kbp plasmid had a single 1 bp discrepancy in a high-copy repeat.
  * The smaller variant is in the Illumina graph (~60x depth) while the larger variant is not.
  * I aligned the long reads, and both seem to prefer the smaller variant in this case.
  * So I'm going to assume that the larger variant is a mistake that Pilon couldn't fix (due to being in a repeat) and change it into the smaller variant.
* The chromosome had 10 single bp discrepancies:
   * 8 were in a very long repeat of the genome, and both Illumina graphs agreed on the correct answer.
   * 1 was on a break in the Illumina graph in rep 1 and I went with the unbroken option in rep 2.
   * The last was a bit weird: a long homopolymer where rep 2 had an exact match to one option and rep 1 didn't match either. Not sure about this one, but I went with the exact match for rep 2 in both.
* Finally, the 17 kbp plasmid has two variants (discovered last time I assembled these genomes) so I included both as 'v1' and 'v2'. Both seem to be present in about a 4:1 ratio of short:long.


So in the end, the two technical replicates were exactly the same except for:
* A 1 bp length difference in the smallest plasmid of barcode 3.
* Two extra small plasmids (at lower depth) in barcode 4.
* One extra small plasmid (at lower depth) in barcode 5.


I then cleaned up the Nanopore reads for assembly, as these were pooled and I'll need to do my analysis on non-pooled reads:
```bash
cd ~/small_plasmids
rm -r */nanopore_reads
```



Finally, I rearrange things a bit, putting all final assemblies in one directory and Illumina reads two others (one for each tech rep):
```bash
cd ~/small_plasmids
mkdir assemblies tech_rep_1_illumina_reads tech_rep_2_illumina_reads
mv tech_rep_*_barcode* assemblies

cd assemblies
mv tech_rep_1_barcode01/tech_rep_1_barcode01.fasta tech_rep_1_Acinetobacter_baumannii_J9.fasta
mv tech_rep_1_barcode02/tech_rep_1_barcode02.fasta tech_rep_1_Citrobacter_koseri_MINF_9D.fasta
mv tech_rep_1_barcode03/tech_rep_1_barcode03.fasta tech_rep_1_Enterobacter_kobei_MSB1_1B.fasta
mv tech_rep_1_barcode04/tech_rep_1_barcode04.fasta tech_rep_1_Haemophilus_unknown_M1C132_1.fasta
mv tech_rep_1_barcode05/tech_rep_1_barcode05.fasta tech_rep_1_Klebsiella_oxytoca_MSB1_2C.fasta
mv tech_rep_1_barcode07/tech_rep_1_barcode07.fasta tech_rep_1_Klebsiella_variicola_INF345.fasta
mv tech_rep_1_barcode08/tech_rep_1_barcode08.fasta tech_rep_1_Serratia_marcescens_17-147-1671.fasta
mv tech_rep_2_barcode01/tech_rep_2_barcode01.fasta tech_rep_2_Acinetobacter_baumannii_J9.fasta
mv tech_rep_2_barcode02/tech_rep_2_barcode02.fasta tech_rep_2_Citrobacter_koseri_MINF_9D.fasta
mv tech_rep_2_barcode03/tech_rep_2_barcode03.fasta tech_rep_2_Enterobacter_kobei_MSB1_1B.fasta
mv tech_rep_2_barcode04/tech_rep_2_barcode04.fasta tech_rep_2_Haemophilus_unknown_M1C132_1.fasta
mv tech_rep_2_barcode05/tech_rep_2_barcode05.fasta tech_rep_2_Klebsiella_oxytoca_MSB1_2C.fasta
mv tech_rep_2_barcode07/tech_rep_2_barcode07.fasta tech_rep_2_Klebsiella_variicola_INF345.fasta
mv tech_rep_2_barcode08/tech_rep_2_barcode08.fasta tech_rep_2_Serratia_marcescens_17-147-1671.fasta
mkdir working_files
mv tech_rep_*_barcode* working_files

cd ~/small_plasmids/tech_rep_1_illumina_reads
mv ../assemblies/working_files/tech_rep_1_barcode01/illumina_reads Acinetobacter_baumannii_J9
mv ../assemblies/working_files/tech_rep_1_barcode02/illumina_reads Citrobacter_koseri_MINF_9D
mv ../assemblies/working_files/tech_rep_1_barcode03/illumina_reads Enterobacter_kobei_MSB1_1B
mv ../assemblies/working_files/tech_rep_1_barcode04/illumina_reads Haemophilus_unknown_M1C132_1
mv ../assemblies/working_files/tech_rep_1_barcode05/illumina_reads Klebsiella_oxytoca_MSB1_2C
mv ../assemblies/working_files/tech_rep_1_barcode07/illumina_reads Klebsiella_variicola_INF345
mv ../assemblies/working_files/tech_rep_1_barcode08/illumina_reads Serratia_marcescens_17-147-1671

cd ~/small_plasmids/tech_rep_2_illumina_reads
mv ../assemblies/working_files/tech_rep_2_barcode01/illumina_reads Acinetobacter_baumannii_J9
mv ../assemblies/working_files/tech_rep_2_barcode02/illumina_reads Citrobacter_koseri_MINF_9D
mv ../assemblies/working_files/tech_rep_2_barcode03/illumina_reads Enterobacter_kobei_MSB1_1B
mv ../assemblies/working_files/tech_rep_2_barcode04/illumina_reads Haemophilus_unknown_M1C132_1
mv ../assemblies/working_files/tech_rep_2_barcode05/illumina_reads Klebsiella_oxytoca_MSB1_2C
mv ../assemblies/working_files/tech_rep_2_barcode07/illumina_reads Klebsiella_variicola_INF345
mv ../assemblies/working_files/tech_rep_2_barcode08/illumina_reads Serratia_marcescens_17-147-1671
```

I also ensured that the sequences in the assemblies all started with their genome name and a double-underscore before the replicon name:
* `Acinetobacter_baumannii_J9__`
* `Citrobacter_koseri_MINF_9D__`
* `Enterobacter_kobei_MSB1_1B__`
* `Haemophilus_unknown_M1C132_1__`
* `Klebsiella_oxytoca_MSB1_2C__`
* `Klebsiella_variicola_INF345__`
* `Serratia_marcescens_17-147-1671__`


And on a final final note, I decided to combine the assemblies into just one per genome (i.e. not one for each tech rep). This is because the genomes were nearly the same, except for some extra plasmids (which I can include) and a single variant in the Enterobacter small plasmid (for which I'll include both variants).

So my final assemblies were:
* Acinetobacter_baumannii_J9
  * chromosome length=3798646 circular=true
  * plasmid_1 length=145059 circular=true
  * plasmid_2 length=6078 circular=true
* Citrobacter_koseri_MINF_9D
  * chromosome length=4758908 circular=true
  * plasmid_1 length=64962 circular=true
  * plasmid_2 length=9294 circular=true
* Enterobacter_kobei_MSB1_1B
  * chromosome length=4837926 circular=true
  * plasmid_1 length=136482 circular=true
  * plasmid_2 length=108411 circular=true
  * plasmid_3 length=4665 circular=true
  * plasmid_4 length=3715 circular=true
  * plasmid_5_v1 length=2370 circular=true
  * plasmid_5_v2 length=2369 circular=true
* Haemophilus_unknown_M1C132_1
  * chromosome length=2051882 circular=true
  * plasmid_1 length=39398 circular=true
  * plasmid_2 length=10719 circular=true
  * plasmid_3 length=9975 circular=true
  * plasmid_4 length=7392 circular=true
  * plasmid_5 length=5675 circular=true
* Klebsiella_oxytoca_MSB1_2C
  * chromosome length=5804453 circular=true
  * plasmid_1 length=118161 circular=true
  * plasmid_2 length=58472 circular=true
  * plasmid_3 length=9975 circular=true
  * plasmid_4 length=4574 circular=true
* Klebsiella_variicola_INF345
  * chromosome length=5417255 circular=true
  * plasmid_1 length=250980 circular=true
  * plasmid_2 length=243620 circular=true
  * plasmid_3 length=31780 circular=false
  * plasmid_4 length=5783 circular=true
  * plasmid_5 length=3514 circular=true
* Serratia_marcescens_17-147-1671
  * chromosome length=5518076 circular=true
  * plasmid_1 length=184477 circular=true
  * plasmid_2 length=161385 circular=true
  * plasmid_3_v1 length=18733 circular=true
  * plasmid_3_v2 length=17406 circular=true
  * plasmid_4 length=1934 circular=true


# Read characterisation

## Prep files

Transfer the reads over:
```bash
cd ~/small_plasmids
mkdir tech_rep_1_ligation_reads
mkdir tech_rep_1_rapid_reads
mkdir tech_rep_2_ligation_reads
mkdir tech_rep_2_rapid_reads

cd ~/small_plasmids/tech_rep_1_ligation_reads
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/minion/2020-01-16_plasmid_ligation/fastq/sequencing_summary.txt.gz" .
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/minion/2020-01-16_plasmid_ligation/fastq/*.fastq.gz" .

cd ~/small_plasmids/tech_rep_1_rapid_reads
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/minion/2020-01-16_plasmid_rapid/fastq/sequencing_summary.txt.gz" .
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/minion/2020-01-16_plasmid_rapid/fastq/*.fastq.gz" .

cd ~/small_plasmids/tech_rep_2_ligation_reads
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/minion/2020-06-10_small_plasmid_ligation_02/fastq/sequencing_summary.txt.gz" .
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/minion/2020-06-10_small_plasmid_ligation_02/fastq/*.fastq.gz" .

cd ~/small_plasmids/tech_rep_2_rapid_reads
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/minion/2020-06-09_small_plasmid_rapid_02/fastq/sequencing_summary.txt.gz" .
scp rwic0002@m3-dtn1.massive.org.au:"/mnt/vault2_holt/vault/instruments/minion/2020-06-09_small_plasmid_rapid_02/fastq/*.fastq.gz" .

```


Combine them into one file and sort them alphabetically:
```bash
cd ~/small_plasmids/tech_rep_1_ligation_reads
zcat *.fastq.gz | paste - - - - | sort | tr '\t' '\n' | gzip > reads.fastq.gz
rm barcode*.fastq.gz unclassified.fastq.gz

cd ~/small_plasmids/tech_rep_1_rapid_reads
zcat *.fastq.gz | paste - - - - | sort | tr '\t' '\n' | gzip > reads.fastq.gz
rm barcode*.fastq.gz unclassified.fastq.gz

cd ~/small_plasmids/tech_rep_2_ligation_reads
zcat *.fastq.gz | paste - - - - | sort | tr '\t' '\n' | gzip > reads.fastq.gz
rm barcode*.fastq.gz unclassified.fastq.gz

cd ~/small_plasmids/tech_rep_2_rapid_reads
zcat *.fastq.gz | paste - - - - | sort | tr '\t' '\n' | gzip > reads.fastq.gz
rm barcode*.fastq.gz unclassified.fastq.gz
```


Sort the sequencing summary files too:
```bash
for d in tech_rep_1_ligation_reads tech_rep_1_rapid_reads tech_rep_2_ligation_reads tech_rep_2_rapid_reads; do
    cd ~/small_plasmids/"$d"
    zcat sequencing_summary.txt.gz | head -n1 > temp
    zcat sequencing_summary.txt.gz | tail -n+2 | sort -k2 >> temp
    rm sequencing_summary.txt.gz
    mv temp sequencing_summary.txt
    gzip sequencing_summary.txt
done
```


Make a directory for the analysis files:
```bash
cd ~/small_plasmids
mkdir data
```





## Align reads

I wrote a little script to align reads to each doubled sequence independently. I found this actually gave me some more alignments than I got from aligning to all the sequences at once, and thus had some consequences for calling chimeras. The cut command is to get rid of the CIGARs which I don't need and use up a lot of file space.
```bash
cd ~/small_plasmids
~/small_plasmids/scripts/align_reads.py tech_rep_1_ligation_reads/reads.fastq.gz assemblies/*.fasta | cut -f1-12 | sort | gzip > data/tech_rep_1_ligation_reads.paf.gz
~/small_plasmids/scripts/align_reads.py tech_rep_1_rapid_reads/reads.fastq.gz assemblies/*.fasta | cut -f1-12 | sort | gzip > data/tech_rep_1_rapid_reads.paf.gz
~/small_plasmids/scripts/align_reads.py tech_rep_2_ligation_reads/reads.fastq.gz assemblies/*.fasta | cut -f1-12 | sort | gzip > data/tech_rep_2_ligation_reads.paf.gz
~/small_plasmids/scripts/align_reads.py tech_rep_2_rapid_reads/reads.fastq.gz assemblies/*.fasta | cut -f1-12 | sort | gzip > data/tech_rep_2_rapid_reads.paf.gz
```




## Gather and combine data

To save some space (and time when loading data into R) I made smaller versions of the sequencing_summary files, keeping only interesting columns:
* column 2:  read_id
* column 7:  start_time
* column 13: template_duration
* column 14: sequence_length_template
* column 15: mean_qscore_template
* column 21: barcode_arrangement
* column 25: barcode_score

One of the runs (tech_rep_2_ligation) was restarted, resulting in two run IDs (d02e7005 and 56548828), each with times starting at zero. I therefore need to shift the times of the reads on the second run (56548828), so I added 5569 seconds to each of those reads (using some awkward awk). This number was 5269 (the highest time on the first run) plus 300 (about 5 minutes between the runs).

```bash
cd ~/small_plasmids
gunzip -c tech_rep_1_ligation_reads/sequencing_summary.txt.gz | cut -f2,7,13,14,15,21,25 | head -n1 > tech_rep_1_ligation_reads/sequencing_summary_small.txt
gunzip -c tech_rep_1_ligation_reads/sequencing_summary.txt.gz | cut -f2,7,13,14,15,21,25 | tail -n+2 | sort >> tech_rep_1_ligation_reads/sequencing_summary_small.txt

gunzip -c tech_rep_1_rapid_reads/sequencing_summary.txt.gz | cut -f2,7,13,14,15,21,25 | head -n1 > tech_rep_1_rapid_reads/sequencing_summary_small.txt
gunzip -c tech_rep_1_rapid_reads/sequencing_summary.txt.gz | cut -f2,7,13,14,15,21,25 | tail -n+2 | sort >> tech_rep_1_rapid_reads/sequencing_summary_small.txt

gunzip -c tech_rep_2_ligation_reads/sequencing_summary.txt.gz | cut -f2,7,13,14,15,21,25 | head -n1 > tech_rep_2_ligation_reads/sequencing_summary_small.txt
gunzip -c tech_rep_2_ligation_reads/sequencing_summary.txt.gz | awk '{if ($3 == "56548828680a595a295a478bb9b401684383f953") {printf $0"\t"; {printf "%6.6f\n", $7+5569}} else {print $0"\t"$7}}' | cut -f2,7,13,14,15,21,25,40 | awk '{print $1"\t"$8"\t"$3"\t"$4"\t"$5"\t"$6"\t"$7}' | tail -n+2 | sort >> tech_rep_2_ligation_reads/sequencing_summary_small.txt

gunzip -c tech_rep_2_rapid_reads/sequencing_summary.txt.gz | cut -f2,7,13,14,15,21,25 | head -n1 > tech_rep_2_rapid_reads/sequencing_summary_small.txt
gunzip -c tech_rep_2_rapid_reads/sequencing_summary.txt.gz | cut -f2,7,13,14,15,21,25 | tail -n+2 | sort >> tech_rep_2_rapid_reads/sequencing_summary_small.txt
```


I then ran my analysis script:
```bash
cd ~/small_plasmids
pypy3 ~/small_plasmids/scripts/assign_reads.py tech_rep_1_ligation_reads/reads.fastq.gz tech_rep_1_ligation_reads/sequencing_summary_small.txt data/tech_rep_1_ligation_reads.paf.gz | gzip > data/tech_rep_1_ligation_reads.tsv.gz
pypy3 ~/small_plasmids/scripts/assign_reads.py tech_rep_1_rapid_reads/reads.fastq.gz tech_rep_1_rapid_reads/sequencing_summary_small.txt data/tech_rep_1_rapid_reads.paf.gz | gzip > data/tech_rep_1_rapid_reads.tsv.gz
pypy3 ~/small_plasmids/scripts/assign_reads.py tech_rep_2_ligation_reads/reads.fastq.gz tech_rep_2_ligation_reads/sequencing_summary_small.txt data/tech_rep_2_ligation_reads.paf.gz | gzip > data/tech_rep_2_ligation_reads.tsv.gz
pypy3 ~/small_plasmids/scripts/assign_reads.py tech_rep_2_rapid_reads/reads.fastq.gz tech_rep_2_rapid_reads/sequencing_summary_small.txt data/tech_rep_2_rapid_reads.paf.gz | gzip > data/tech_rep_2_rapid_reads.tsv.gz
```


Then aligning Illumina reads:
```bash
for genome in Acinetobacter_baumannii_J9 Citrobacter_koseri_MINF_9D Enterobacter_kobei_MSB1_1B Haemophilus_unknown_M1C132_1 Klebsiella_oxytoca_MSB1_2C Klebsiella_variicola_INF345 Serratia_marcescens_17-147-1671; do
    a=~/small_plasmids/assemblies/"$genome".fasta
    cd ~/small_plasmids/tech_rep_1_illumina_reads/"$genome"
    printf "\n"$genome"\n"
    bowtie2-build "$a" "$a" &> /dev/null
    bowtie2 -1 trimmed_1.fastq.gz -2 trimmed_2.fastq.gz -U trimmed_u.fastq.gz -x "$a" --sensitive-local --threads 16 -I 150 -X 800 | samtools sort > "$genome".bam
    samtools index "$genome".bam
    printf "\n"
done

for genome in Acinetobacter_baumannii_J9 Citrobacter_koseri_MINF_9D Enterobacter_kobei_MSB1_1B Haemophilus_unknown_M1C132_1 Klebsiella_oxytoca_MSB1_2C Klebsiella_variicola_INF345 Serratia_marcescens_17-147-1671; do
    a=~/small_plasmids/assemblies/"$genome".fasta
    cd ~/small_plasmids/tech_rep_2_illumina_reads/"$genome"
    printf "\n"$genome"\n"
    bowtie2-build "$a" "$a" &> /dev/null
    bowtie2 -1 trimmed_1.fastq.gz -2 trimmed_2.fastq.gz -U trimmed_u.fastq.gz -x "$a" --sensitive-local --threads 16 -I 150 -X 800 | samtools sort > "$genome".bam
    samtools index "$genome".bam
    printf "\n"
done

rm ~/small_plasmids/assemblies/*.bt2
```







## Get depths

For Nanopore reads:
```bash
cd ~/small_plasmids
scripts/get_depths.py assemblies data/tech_rep_1_ligation_reads.tsv.gz
scripts/get_depths.py assemblies data/tech_rep_1_rapid_reads.tsv.gz
scripts/get_depths.py assemblies data/tech_rep_2_ligation_reads.tsv.gz
scripts/get_depths.py assemblies data/tech_rep_2_rapid_reads.tsv.gz
```

And for Illumina reads:
```bash
cd ~/small_plasmids
for b in tech_rep_1_illumina_reads/*/*.bam; do
    scripts/get_depths.py assemblies $b
done

for b in tech_rep_2_illumina_reads/*/*.bam; do
    scripts/get_depths.py assemblies $b
done
```

I pasted all of this depth data into the Excel spreadsheet: `data.xlsx`. For plasmids with two versions, I added the depths of the two versions together to get a single depth for that plasmid.

Also I got the GC content of the assemblies:
```bash
cd ~/small_plasmids
scripts/get_gc.py assemblies
```





## Depth vs GC

I wanted to assess whether or not the GC bias in Illumina sequencing might require correction, so 

```bash
cd ~/small_plasmids

echo "gc\tdepth" > gc_and_depth.tsv

scripts/depth_and_gc.py assemblies/Acinetobacter_baumannii_J9.fasta tech_rep_1_illumina_reads/Acinetobacter_baumannii_J9/Acinetobacter_baumannii_J9.bam >> gc_and_depth.tsv
scripts/depth_and_gc.py assemblies/Citrobacter_koseri_MINF_9D.fasta tech_rep_1_illumina_reads/Citrobacter_koseri_MINF_9D/Citrobacter_koseri_MINF_9D.bam >> gc_and_depth.tsv 
scripts/depth_and_gc.py assemblies/Enterobacter_kobei_MSB1_1B.fasta tech_rep_1_illumina_reads/Enterobacter_kobei_MSB1_1B/Enterobacter_kobei_MSB1_1B.bam >> gc_and_depth.tsv  
scripts/depth_and_gc.py assemblies/Haemophilus_unknown_M1C132_1.fasta tech_rep_1_illumina_reads/Haemophilus_unknown_M1C132_1/Haemophilus_unknown_M1C132_1.bam >> gc_and_depth.tsv
scripts/depth_and_gc.py assemblies/Klebsiella_oxytoca_MSB1_2C.fasta tech_rep_1_illumina_reads/Klebsiella_oxytoca_MSB1_2C/Klebsiella_oxytoca_MSB1_2C.bam >> gc_and_depth.tsv
scripts/depth_and_gc.py assemblies/Klebsiella_variicola_INF345.fasta tech_rep_1_illumina_reads/Klebsiella_variicola_INF345/Klebsiella_variicola_INF345.bam >> gc_and_depth.tsv
scripts/depth_and_gc.py assemblies/Serratia_marcescens_17-147-1671.fasta tech_rep_1_illumina_reads/Serratia_marcescens_17-147-1671/Serratia_marcescens_17-147-1671.bam >> gc_and_depth.tsv

scripts/depth_and_gc.py assemblies/Acinetobacter_baumannii_J9.fasta tech_rep_2_illumina_reads/Acinetobacter_baumannii_J9/Acinetobacter_baumannii_J9.bam >> gc_and_depth.tsv
scripts/depth_and_gc.py assemblies/Citrobacter_koseri_MINF_9D.fasta tech_rep_2_illumina_reads/Citrobacter_koseri_MINF_9D/Citrobacter_koseri_MINF_9D.bam >> gc_and_depth.tsv 
scripts/depth_and_gc.py assemblies/Enterobacter_kobei_MSB1_1B.fasta tech_rep_2_illumina_reads/Enterobacter_kobei_MSB1_1B/Enterobacter_kobei_MSB1_1B.bam >> gc_and_depth.tsv  
scripts/depth_and_gc.py assemblies/Haemophilus_unknown_M1C132_1.fasta tech_rep_2_illumina_reads/Haemophilus_unknown_M1C132_1/Haemophilus_unknown_M1C132_1.bam >> gc_and_depth.tsv
scripts/depth_and_gc.py assemblies/Klebsiella_oxytoca_MSB1_2C.fasta tech_rep_2_illumina_reads/Klebsiella_oxytoca_MSB1_2C/Klebsiella_oxytoca_MSB1_2C.bam >> gc_and_depth.tsv
scripts/depth_and_gc.py assemblies/Klebsiella_variicola_INF345.fasta tech_rep_2_illumina_reads/Klebsiella_variicola_INF345/Klebsiella_variicola_INF345.bam >> gc_and_depth.tsv
scripts/depth_and_gc.py assemblies/Serratia_marcescens_17-147-1671.fasta tech_rep_2_illumina_reads/Serratia_marcescens_17-147-1671/Serratia_marcescens_17-147-1671.bam >> gc_and_depth.tsv

gzip gc_and_depth.tsv
```
