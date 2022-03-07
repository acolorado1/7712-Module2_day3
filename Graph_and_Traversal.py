'''
Author: Angela Sofia Burkhart Colorado
Date: February 25th, 2022
Purpose: This program is supposed take several sequences, find all kmers (edges), get k-1mers (nodes), create an
adjacency list of them (graph) and using DFS (Depth First Search) graph traversal get all possible paths in the graph.
These paths will then take the nodes and create all possible contigs with starting nodes being those that only have
edges pointing away from them.
'''

# get kmers (these are the edges)
def kmers (reads, k):
    kmers = []
    # for every read in dictionary of reads
    for key in reads:
        read = reads[key]
        # for every fragment of k length
        for index in range(0,len(read)-k + 1):
            kmers.append(read[index: index + k])
    # list of k-length fragments (strings)
    return kmers


# get the k-1mers (these will be the nodes), take each kmer and take the first k-1 characters (prefix) and the last k-1
# characters (suffix)
def k_1mers (kmers):
    nodes = set()
    for kmer in kmers:
        # add to set tuple of kmer prefix and suffix
        nodes.add((kmer[:-1], kmer[1:]))
    # return set of tuples (prefix, suffix)
    return nodes


# get adjacency list of nodes
def adjacency_list(nodes):
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
        # add second item in tuple to list of first item in tuple
        adj_list[pair[0]].append(pair[1])
    # return a dictionary containing each node (keys) and the nodes they connect to (directed) as a list (values)
    return adj_list


# using depth first search (DFS) graph traversal get all nodes in a path
def graph_traversal(adjacency_list, startnode,  visited=None):
    # if the object visited is a None object
    if visited is None:
        # initialize visited list
        visited = []
    # if the start node is not in the visited list
    if startnode not in visited:
        # append start node to visited list
        visited.append(startnode)
        # for the next node in the sequence taken from list (value) of startnode (key)
        for neighbour in graph[startnode]:
            # call graph_traversal function to get the following node
            graph_traversal(adjacency_list, neighbour, visited)
    # return list of visited node or path
    return visited


# get all start and ending nodes
def list_startnodes_endnodes(tuple_nodes):
    temp_startnode_list = []
    temp_endnode_list = []
    # for every tuple of connected nodes
    for tuple in tuple_nodes:
        # append node in the first index
        temp_startnode_list.append(tuple[0])
        # append node in the second index
        temp_endnode_list.append(tuple[1])
    # find all nodes that are in the first position of the tuple but not in the second
    start_set_difference = set(temp_startnode_list) - set(temp_endnode_list)
    # find all nodes that are in the second position of the tuple but not in the first
    end_set_difference = set(temp_endnode_list) - set(temp_startnode_list)
    startnodes = list(start_set_difference)
    endnodes = list(end_set_difference)
    # return tuple of start nodes list and end nodes list
    return startnodes, endnodes


# use all nodes in the startnodes list as all startnodes to possible paths/contigs
def startnode(startnodes, adjacency_list):
    contigs = []
    # for each node (key) in the adjacency_list dictionary
    for startnode in startnodes:
        # find path using node as startnode
        graph = graph_traversal(adjacency_list, startnode)
        # append path to list
        contigs.append(graph)
    # return list of lists containing paths
    return contigs


# take list of lists with paths and create string contigs
def contigs(listoflistcontigs, endnodes):
    stringcontigs = []
    # for each list of nodes in path
    for contiglist in listoflistcontigs:
        contig = ''
        # if the last node in the contiglist is a node in the endnodes list
        if contiglist[-1] in endnodes:
            # for every node
            for index in range(len(contiglist)):
                # if the fist node
                if index == 0:
                    # add node to contig string
                    contig += contiglist[index]
                # if not first node
                else:
                    # add the last character in node string to contig string
                    contig += contiglist[index][-1]
            # append full contig from path to list
            stringcontigs.append(contig)
    # return list of possible contigs
    return stringcontigs

read = {1: "MYDOGMAX"}
reads = {1: "MYDOGMAX", 2: "MYDOGSMOKEY"}
edges = kmers(reads, 4)
nodes = k_1mers(edges)
graph = adjacency_list(nodes)
start_end_nodes = list_startnodes_endnodes(nodes)
startnodes = start_end_nodes[0]
endnodes = start_end_nodes[1]
listoflistscontigs = startnode(startnodes, graph)

print('edges: ', edges)
print('nodes: ', nodes)
print('graph: ', graph)
print('startnodes: ', startnodes)
print('endnodes: ', endnodes, '\n')


print(contigs(listoflistscontigs, endnodes))
