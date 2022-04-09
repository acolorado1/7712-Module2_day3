'''
Author: Angela Sofia Burkhart Colorado
Date: February 25th, 2022
Purpose: This program takes several sequences, find all kmers (edges), get k-1mers (nodes), create an
adjacency list of them (graph) and using DFS (Depth First Search) graph traversal get all possible paths in the graph.
Sets of starting nodes (those nodes with an in-degree of 0) and ending nodes (those nodes with an out-degree of 0) will
be found and the smaller list will be used as starting nodes for graph traversal and contig creation. Output will be a
dictionary containing all traversed nodes in all paths, and the constructed contig from each path.
'''


# create class Edge with attributes: sequence, starting position, ending position, and FASTA ID
class Edge:
    def __init__(self, readID, start, end, seq):
        self.ID = readID
        self.s = start
        self.e = end
        self.seq = seq

    # Make object hashable
    def __hash__(self):
        return hash(self.seq)

    # when comparing with other objects of same class compare sequence attribute
    def __eq__(self, other):
        return self.seq == other.seq

    # to avoid having self and other object of same class be equal and not equal to each other at the same time
    def __ne__(self, other):
        return not (self == other)

# create class Node with attributes: sequence, starting position, ending position, and FASTA ID
class Node:
    def __init__(self, readID, start, end, seq):
        self.ID = readID
        self.s = start
        self.e = end
        self.seq = seq

    # Make object hashable
    def __hash__(self):
        return hash(self.seq)

    # when comparing with other objects of same class compare sequence attribute
    def __eq__(self, other):
        return self.seq == other.seq

    # to avoid having self and other object of same class be equal and not equal to each other at the same time
    def __ne__(self, other):
        return not (self == other)


# get kmers (these are the edges)
def kmers(reads, k, largest_sequence):
    # if k is smaller than or equal to the shortest read
    if k <= largest_sequence:
        kmers = []
        # for every read in dictionary of reads
        for key in reads:
            read = reads[key]
            # for every fragment of k length
            for index in range(0,len(read)-k + 1):
                # assign to starting position the current index
                startposition = index
                # assign to ending position the current index plus k minus one
                endposition = index + k -1
                # splice read from starting position to ending position
                sequence = read[index: index + k]
                # create Edge objects with attributes
                edge = Edge(key, startposition, endposition, sequence)
                # append to list
                kmers.append(edge)
    # else write exception message warning that k is larger than shortest read
    else:
        raise Exception("k is larger than the shortest read, pick k smaller than", largest_sequence)
    # list of k-length fragments (strings)
    return kmers


# get the k-1mers (these will be the nodes), take each kmer and take the first k-1 characters (prefix) and the last k-1
# characters (suffix)
def k_1mers(kmers):
    nodes = set()
    for kmer in kmers:
        # get prefix node attributes
        prefixID = kmer.ID
        prefixstart = kmer.s
        prefixend = kmer.e - 1
        prefixseq = kmer.seq[:-1]

        # get suffix node attributes
        suffixID = kmer.ID
        suffixstart = kmer.s + 1
        suffixend = kmer.e
        suffixseq = kmer.seq[1:]

        # create prefix and suffix node objects
        prefix = Node(prefixID, prefixstart, prefixend, prefixseq)
        suffix = Node(suffixID, suffixstart, suffixend, suffixseq)

        # append prefix and suffix as tuple to set
        nodes.add((prefix, suffix))
    # return set of tuples (prefix, suffix)
    return nodes


# get adjacency list of nodes
def adjacency_list(nodes, start=False):
    adj_list = {}
    # for each tuple
    for pair in nodes:
        # if the first item in the tuple (node) is not a key in adj_list dictionary
        if pair[0] not in adj_list.keys():
            # add it as a key with empty list value
            adj_list[pair[0]] = []
        # if the second item in the tuple (node) is not a key in adj_list dictionary
        if pair[1] not in adj_list.keys():
            # add it as a key with empty list value
            adj_list[pair[1]] = []
        if start == False:
            # add second item in tuple to list of first item in tuple
            adj_list[pair[1]].append(pair[0])
        else:
            # add first item in tuple to list of second item in a tuple
            adj_list[pair[0]].append(pair[1])
    # return a dictionary containing each node (keys) and the nodes they connect to (directed) as a list (values)
    return adj_list


# using depth first search (DFS) graph traversal get all nodes in a path
def graph_traversal(adjacency_list, startnode, start = False):
    # initiate stack
    stack = []
    # initiate list of visited nodes
    visited = []
    stack.append(startnode)

    # while the length of the stack is not equal to 0
    while len(stack) != 0:
        # get the last value from the stack
        newNode = stack.pop()
        # if last value of stack is not in visited
        if newNode not in visited:
            # append to the list of visited nodes
            visited.append(newNode)
        # for every vertex that is connected to the current node or last node in stack
        for neighbor in adjacency_list[newNode]:
            # if the node has not bee visited
            if neighbor not in visited:
                # add to the stack
                stack.append(neighbor)
    # if you use endnodes as starting nodes in the traversal
    if start == False:
        # reverse the contig
        visited.reverse()
    # return the list of visited nodes to find path
    return visited


# get all start (in-degree is equal to 0) and end nodes (out-degree is equal to 0)
def startnodes_endnodes(node_tuples):
    # initiate temporary set of potential start nodes
    temp_startnodes = set()
    # initiate temporary set of potential end nodes
    temp_endnodes = set()
    # for every tuple of connected nodes
    for pair in node_tuples:
        # add x value to start node set
        temp_startnodes.add(pair[0])
        # add y value to end node set
        temp_endnodes.add(pair[1])
    # get difference between end node and start node sets to get true set of end nodes
    end_set_difference = temp_endnodes - temp_startnodes
    # get difference between star and end node sets to get true set of start nodes
    start_set_difference = temp_startnodes - temp_endnodes
    # create dictionary of start and end nodes
    start_end_dict = {"startnodes": start_set_difference, "endnodes": end_set_difference}
    return start_end_dict


# traversing the graph using all detected end or start nodes
def all_traversals(nodes, graph, start = False):
    # initiate list of paths created
    path_count = 1
    paths = {}
    # for every found endnode
    for node in nodes:
        # find path using endnode
        path = graph_traversal(graph, node, start)
        # append path to list of paths
        paths[path_count] = path
        # add to path count
        path_count += 1
    # return dictionary containing all paths
    return paths


# take list of lists with paths and create string contigs
def contigs(paths):
    contig_count = 1
    stringcontigs = {}
    # for each list of nodes in path
    for key in paths:
        path = paths[key]
        contig = ''
        # for every node
        for index in range(len(path)):
            # if the fist node
            if index == 0:
                # add node to contig string
                contig += path[index].seq
            # if not first node
            else:
                # add the last character in node string to contig string
                contig += path[index].seq[-1]
            # add contig number and contig to dictionary
            stringcontigs[contig_count] = contig
        contig_count += 1
    # return list of possible contigs
    return stringcontigs

