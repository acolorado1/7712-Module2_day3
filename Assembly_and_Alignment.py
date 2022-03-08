'''
Author: Angela Sofia Burkhart Colorado
Date: March 6th, 2022
Purpose: This program will take a set of sequenced reads and a query sequence and aligns the reads to create contigs
containing the query sequence. It then outputs two files one that has the longest assembled contig that contains the
query sequence, and the other is a file containing alignment information about the contigs. Currently only assembles
the sequences into contigs.
'''

import argparse as arg
import Graph_and_Traversal
import FileReadIn

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


def assemble_and_align(query_file, reads_file, k):
    query = FileReadIn.query_sequence(query_file)
    shortestread_scaffolds_reads = FileReadIn.reads(reads_file)

    edges = Graph_and_Traversal.kmers(shortestread_scaffolds_reads[2], k, shortestread_scaffolds_reads[0])
    nodes = Graph_and_Traversal.k_1mers(edges)
    graph = Graph_and_Traversal.adjacency_list(nodes)
    start_end_nodes = Graph_and_Traversal.list_startnodes_endnodes(nodes)
    startnodes = start_end_nodes[0]
    listoflistscontigs = Graph_and_Traversal.startnode(startnodes, graph)
    contigs = Graph_and_Traversal.contigs(listoflistscontigs)

    print('query sequence: ', query)
    print('shortest read: ', shortestread_scaffolds_reads[0])
    print('example reads: {2S43D:03629:08794,', shortestread_scaffolds_reads[2]["2S43D:03629:08794"], '}\n')

    return contigs

print(assemble_and_align(args.qf, args.rf, args.k))

query_file = "C:\\Users\\ascol\\OneDrive\\Desktop\\7712\\QUERY.fasta"
file_reads = "C:\\Users\\ascol\\OneDrive\\Desktop\\7712\\READS.fasta"
#reads = {1: "MYDOGMAX", 2: "MYDOGSMOKEY"}

