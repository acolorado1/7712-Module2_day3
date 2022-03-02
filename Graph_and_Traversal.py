'''
Author: Angela Sofia Burkhart Colorado
Date: February 25th, 2022
Purpose: This program is supposed take several sequence reads from a file and generate a de bruijn graph that will be
traversed in order to create and find the largest contig sequences.
'''

import toyplot
import numpy as np

'''
parser arguments go here 
'''


# Get k-mers
def kmer(reads, k):
    kmers = []
    # for each sequence
    for key in reads:
        seq = reads[key]
        # index sequence from current index to index + k
        for index in range(0,len(seq)-k+1):
            kmers.append(seq[index:index+k])
    return kmers


# Count number of times a unique kmer appeared
def count_kmers(kmers):
    # find all unique kmers
    unique_kmers = list(set(kmers))
    kmer_dict = {}
    # generate empty dictionary with unique kmers (keys) and 0 (values)
    for item in unique_kmers:
        kmer_dict[item] = 0
    # count how many times they appeared
    for kmer in kmers:
        kmer_dict[kmer] += 1
    return kmer_dict


# Get all edges by finding which k-1mers overlap
def edges(kmers_and_counts, k):
    edges = set()
    last_kmer = []
    # compare kmer k-1mers to find overlaps
    for kmer1 in kmers_and_counts:
        for kmer2 in kmers_and_counts:
            # if the kmer is not the same
            if kmer1 != kmer2:
                if kmer1[1:] == kmer2[0:k-1]:
                    edges.add((kmer1[0:k-1], kmer2[0:k-1]))
                    # get potential last k-1mer pair
                    last_kmer.append((kmer1[1:], kmer2[1:]))
                if kmer1[0:k-1] == kmer2[1:]:
                    edges.add((kmer2[0:k-1], kmer1[0:k-1]))
    for pair in last_kmer:
        if pair not in edges:
            edges.add(pair)
    return edges



# TODO
# Plot graph
def plot_graph(edges):
    # return graph made using toyplot
    graph_edges = np.array(edges)
    graph = toyplot.graph(graph_edges, ewidth=1.0)
    return graph


# Creates a dictionary of all node pairs containing k-1mers
def graph_dict (edges):
    graph = {}
    for pair in edges:
        node1 = pair[0]
        node2 = pair[1]
        if node1 not in graph.keys():
            graph[node1] = []
        graph[node1].append(node2)
    return graph


# using Depth First Traversal find a potential contig
def dfs(startnode, graph, previousnode=None):
    visited = []
    visited.append(startnode)
    tempgraph = graph
    nextnode = tempgraph[startnode][0]
    # while next node is not the last node
    while nextnode in list(tempgraph):
        visited.append(nextnode)
        # if not the first node
        if previousnode is not None:
            del tempgraph[previousnode]
        previousnode = startnode
        startnode = nextnode
        nextnode = tempgraph[startnode][0]
    visited.append(nextnode)
    return visited



# test all k-1mers as starting node to find largest contig
def largest_contig(graph):
    largest = ""
    for key in graph:
        contig = dfs(key, graph)
        print(graph)
        print(contig)
        if len(largest) < len(contig):
            largest = contig
    return largest


# TODO
# turn largest contig from a list to a string sequence
def listtosequnce (largest_contig):
    sequence = ""
    for index in range(len(largest_contig)):
        if index == 0:
            sequence += largest_contig[index]
        else:
            k_1mer = largest_contig[index]
            sequence += k_1mer[-1]
    return sequence


read = {1:"MYDOGMAX"}
reads = {1:"MYDOGMAX", 2:"MYDOGSMOKEY"}
kmers = kmer(reads, 4)
kmer_counts = count_kmers(kmers)
edges = edges(kmer_counts,4)
graph = graph_dict(edges)
print(graph)

#print(dfs("MYD", graph))
#largest_contig = largest_contig(graph)

#seq = listtosequnce(largest_contig)



