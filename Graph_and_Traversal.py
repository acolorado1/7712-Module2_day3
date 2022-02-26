'''
Author:
Date:
Purpose:
'''

import random
import toyplot

'''
parser arguments go here 
'''

read = {1:"MYDOGMAX"}
reads = {1:"MYDOGMAX", 2:"MYDOGSMOKEY"}

# TODO
# Get k-mers
def kmer(reads, k):
    # divide reads into k-length fragments
    # return list of kmers

# TODO
# Count number of times a unique kmer appeared
def count_kmers(kmers):
    # find all unique kmers
    # count how many times they appeared
    # return dictionary of kmers (keys) and counts (value)

# TODO
# Get all edges by finding which k-1mers overlap
def edges (kmers_and_counts):
    # get k-1mers
    # compare their beginning and end to find overlaps
    # return a dictionary of tuples with k-1mers

# TODO
# Plot graph
def plot_graph(edges):
    # return graph made using toyplot