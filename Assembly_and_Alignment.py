'''
Author: Angela Sofia Burkhart Colorado
Date: March 6th, 2022
Purpose: This program takes a set of sequenced reads and a query sequence and aligns the reads to create contigs
containing the query sequence. It then outputs two files one that has the longest assembled contig that contains the
query sequence, and the other is a file containing alignment information about the contigs.
'''

import Graph_and_Traversal
import FileReadIn

'''
parser
'''

query_file = "C:\\Users\\ascol\\OneDrive\\Desktop\\7712\\QUERY.fasta"
file_reads = "C:\\Users\\ascol\\OneDrive\\Desktop\\7712\\READS.fasta"

query = FileReadIn.query_sequence(query_file)
shortestread_scaffolds_reads = FileReadIn.reads(file_reads)


print('query sequence: ', query)
print('shortest read: ', shortestread_scaffolds_reads[0])
print('scaffold :', shortestread_scaffolds_reads[1])
print('reads: 2S43D:03629:08794,', shortestread_scaffolds_reads[2]["2S43D:03629:08794"], '\n')


reads = {1: "MYDOGMAX", 2: "MYDOGSMOKEY"}
edges = Graph_and_Traversal.kmers(reads, 30)
nodes = Graph_and_Traversal.k_1mers(edges)
graph = Graph_and_Traversal.adjacency_list(nodes)
start_end_nodes = Graph_and_Traversal.list_startnodes_endnodes(nodes)
startnodes = start_end_nodes[0]
endnodes = start_end_nodes[1]
listoflistscontigs = Graph_and_Traversal.startnode(startnodes, graph)
contigs = Graph_and_Traversal.contigs(listoflistscontigs, endnodes)



print('edges: ', edges)
print('nodes: ', nodes)
print('graph: ', graph)
print('startnodes: ', startnodes)
print('endnodes: ', endnodes, '\n')
print('contigs: ', contigs)


