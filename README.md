# Sequence Assembly and Alignment

## Description 

This program currently takes one FASTA formatted file containing multiple sequence reads and assembles them into larger
contigs. It also takes one FASTA formatted file containing a query sequence, and aligns the query sequence to the 
assembled contigs. The largest contigs containing the query sequence are then output in a file names ALLELES.fasta, and 
information about their alignment (e.g. FASTA read ID, alignment starting and end positions, etc.) are output in a file 
named ALLELES.aln. 

## Workflow

### Arguments 

Here is a list of required and optional arguments that can be accessed by 
typing **python "Assembly_and_Alignment.py" -h**: 

```text
usage: Assembly_and_Alignment.py [-h] [--qf QF] [--rf RF] [--k K]

Takes a FASTA formatted file containing reads and assembles them into contigs

optional arguments:
  -h, --help            show this help message and exit
  --qf QF, -query_file QF
                        file path containing query sequence
  --rf RF, -reads_file RF
                        file path containing reads
  --k K, -kmer_lenght K
                        number of kmer length

```
### Inputs 

Requires file path of FASTA file containing query sequence, and file path of FASTA file containing sequence reads, as 
well as the length of the kmers. 

Query sequence FASTA file example: 

```text
>INITIAL_QUERY
GGGATCGGCCATTGAACAAGATGGATTGCACGCAGGTTCTCCGGCCGCTTGGGTGGAGAGGCTATTCGGCTATGACTGGGCACAACAGACAATCGGCTGCTCTGATGCCGCCGTGTT
```

Reads FASTA file example: 

```text
>2S43D:03629:08794
TTCAGGCTCTGGCATGCATTAGAAATGTGGCTTGTTTT
>2S43D:08938:01257
GGGTGGTCCCCCTCCTTTACTTGTAACGTTGTCCTAAGTCGTTTTCTTTAGCCCATGGTGTTGGTGGGGTTCACAGAAACACCCAGAGTTCACCTGAGCCTTTAACCAATCCCAGCCCAGGGAGCCAGAGCCCAGGCACAGGTGCAGGACCACGGCAGGCCCAGTATTGGCTCCGACAGAAGCTACGGCATCCTATCGAGTGCACTGGGCTCGTGGTGGGAAGCAGGACA
>2S43D:05292:10188
GGGTGGTCTCCTTTACTTGTAACTTGTCCTAAGTCGTTTCTTTAGCCCATGGTGTTGGTGGGGTTCACAGAAACACCCAGAGTTCACCTGAGCCTTTAACCAATCCCAGCCAGGAGCCAGAGCCCAGGCACAGGTGCAGGACCACGGCAGGCCCAGTATTTGGCTTCCACAGAAGCTACGGCATCCTGATG
>2S43D:03619:08385
CAACAGGGTTTTGGAAATTTGCCCATTTGCATGGCGAAGACCACCTCTCTCTCTCTCATCGACCT
```
### Command

To run this program in the command line interface type: 
```text
python "Assembly_and_Alignment.py" --qf "QUERY.fasta" --rf "READS.fasta" --k 4
```
You can replace --qf and --rf with your own desired input files as well as change 
the kmer length (--k). 

To run this program interactively type: 


```python
Assembly_and_Alignment("QUERY.fasta", "READS.fasta", 4)
```
If the input files are located in a different directory then you can specify their respective file paths. 

### Output 

This program will output two file: ALLELES.fasta and ALLELES.aln. 

Example of ALLELES.fasta output: 

These contigs were assembled and aligned with test reads and query sequence using input files **QUERY_test.fasta** and 
**READS_test.fasta**. Data from real reads and query sequences can be found in files **QUERY_realdata_test.fasta** and 
**READS_realdata_test.fasta**.

```text
>2G5Z1: contig1
MYGODREUBENWIN
>2G5Z3: contig1
MYDOGMAXSMOKEY
```

Example of ALLELES.aln output: 

```text
sseqid 	                qseqid 	    sstart 	    send 	 qstart     qend 	 pcutoff
2G5Z1:02016:13108 	 contig1 	 4 	        2 	    4 	        2 	 1.0
2G5Z3:02016:13108 	 contig1 	 2 	        4 	    2 	        4 	 1.0
```

Note: tabs in example were adjusted to be more readable. Each item will be followed by only one tab.

## Installation and Dependencies
You must have Python 3 installed. Any Python 3 version should work, but it was written in Python 3.9 using a Windows-based 
operating system. Package argparse 1.4.0 will need to be installed. 

## Contact 
Angela Sofia Burkhart Colorado - angelasofia.burkhartcolorado@cuanschutz.edu

Project Link: https://github.com/acolorado1/7712-Module2_day3.git