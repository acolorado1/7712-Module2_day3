'''
Author: Angela Sofia Burkhart Colorado
Date: March 6th, 2022
Purpose: This program will take a set of sequenced reads and a query sequence and aligns the reads to create contigs
containing the query sequence. It then outputs two files one that has the longest assembled contig that contains the
query sequence, and the other is a file containing alignment information about the contigs. Currently only assembles
the sequences into contigs.
'''

import argparse as arg
import FileReadIn
import Graph_and_Traversal
from src import Alignment
import Output_Files
import time

'''
Added 3 arguments to parser: 
1.--qf parameter that takes the query FASTA file path as string 
2.--rf parameter that takes the file path containing reads in FASTA format as string 
3. --k parameter that takes kmer length as an integer 
'''

parser = arg.ArgumentParser(description="Takes a FASTA formatted file containing reads and assembles them into contigs")
parser.add_argument("--qf", "-query_file", type=str, help="file path containing query sequence", default="QUERY.fasta")
parser.add_argument("--rf", "-reads_file", type=str, help="file path containing reads", default="READS.fasta")
parser.add_argument("--k", "-kmer_lenght", type=int, help="number of kmer length ", default=4)

args = parser.parse_args()


# this function utilizes all the functions for graph traversal and outputs and dictionary where keys are scaffolds and
# values are dictionaries containing paths found through DFS graph traversal and their respective contigs.
def assemble(shortestread_scaffolds_reads, k):
    # create dictionary of dictionaries with the format {scaffold : {readID: read, ...}, ...}
    dict_reads_per_scaffold = FileReadIn.divide_by_scaffold(shortestread_scaffolds_reads)

    # initiate dictionary containing paths and contigs per scaffold
    scaffold_assembly_info = {}

    # for each dictionary containing reads per scaffold
    for scaffold in dict_reads_per_scaffold:
        # initate variable of dictionary containing only FASTA read IDs (keys) and the reads (values)
        dict_of_reads = dict_reads_per_scaffold[scaffold]
        # get kmers of length k which will be the edges of the graph
        edges = Graph_and_Traversal.kmers(dict_of_reads, k, shortestread_scaffolds_reads["shortest_read"])
        # get nodes which are the prefix and suffix of the kmers, output is a list of tuples
        nodes = Graph_and_Traversal.k_1mers(edges)
        # get potential starting (in-edgree equal to 0) and ending (out-degree equal to 0) nodes
        start_end_nodes = Graph_and_Traversal.startnodes_endnodes(nodes)
        startnodes = start_end_nodes["startnodes"]
        endnodes = start_end_nodes["endnodes"]
        # if the set of start nodes is larger than the set of endnodes use endnodes to create graph and traverse it
        if len(startnodes) > len(endnodes):
            graph = Graph_and_Traversal.adjacency_list(nodes, start=False)
            paths = Graph_and_Traversal.all_traversals(endnodes, graph, start=False)
        # otherwise use the startnodes to create and traverse the graph
        else:
            graph = Graph_and_Traversal.adjacency_list(nodes, start=True)
            paths = Graph_and_Traversal.all_traversals(startnodes, graph, start=True)
        # generate contigs from corresponding paths
        contigs = Graph_and_Traversal.contigs(paths)
        # for each scaffold add paths and contigs to dictionary
        scaffold_assembly_info[scaffold] = {"paths": paths, "contigs": contigs}
    # returns dictionary with format: {scaffoldID: {"path": {paths}, "contigs":{contigs}}, ...}
    return scaffold_assembly_info


# takes all contigs and aligns them to the query sequence using functions from the Alignment file
def align(contig_info, query_seq):
    # initalize empty dictionary that will contain alignment information
    aligned_contigs = {}
    # for each scaffold
    for scaffold in contig_info:
        # grab all contigs
        contigs = contig_info[scaffold]["contigs"]
        # for every contig
        for key in contigs:
            # get contig sequence
            contig = contigs[key]
            # if the length of the sequence is greater than or equal to the length of the query perform alignment
            if len(contig) >= len(query_seq):
                alignment_info = Alignment.cutoff_percent_test([contig], query_seq, key)
                # if alignment is found
                if alignment_info != None:
                    # append information to dictionary
                    aligned_contigs[scaffold + ":" + str(key)] = alignment_info
    return aligned_contigs



# combines results of assembly and alignment and uses functions from Output_Files to generate final files containing
# largest assembled sequences containing query sequence and their alignment information
def assemble_and_align(query_file, reads_file, k):
    # get query sequence
    query = FileReadIn.query_sequence(query_file)
    # get length of shortest read, set of scaffolds, and dictionary of reads
    shortestread_scaffolds_reads = FileReadIn.reads(reads_file)

    # get paths and contig information from assembly
    t1 = time.time()
    contig_info = assemble(shortestread_scaffolds_reads, k)
    t2 = time.time()
    print("All paths found, time elapsed: ", t2-t1)
    # get alignment information
    alignment_info = align(contig_info, query)
    t3 = time.time()
    print("Alignment performed, time elapsed: ", t3-t2)
    # get dictionary of largest aligned contigs and output file containing their sequences
    t4 = time.time()
    scaffolds = shortestread_scaffolds_reads["scaffolds"]
    largest_output_file = Output_Files.largest_contig(alignment_info, scaffolds)
    print("File with largest contigs created, time elapsed: ", t4-t3)
    # generate file containing alignment information on the largest contigs
    Output_Files.contig_information(contig_info, alignment_info, largest_output_file, k)
    t5 = time.time()
    print("File with alignment information created, time elapsed: ", t5-t4)
    exit()


#assemble_and_align(args.qf, args.rf, args.k)

assemble_and_align("../Example_data/QUERY_test.fasta", "READS_test.fasta", 4)