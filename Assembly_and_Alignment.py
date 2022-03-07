'''
Author:
Date:
Purpose:
'''

import Graph_and_Traversal

'''
parser
'''

reads = {1: "MYDOGMAX", 2: "MYDOGSMOKEY"}
edges = Graph_and_Traversal.kmers(reads, 4)
nodes = Graph_and_Traversal.k_1mers(edges)
graph = Graph_and_Traversal.adjacency_list(nodes)
start_end_nodes = Graph_and_Traversal.list_startnodes_endnodes(nodes)
startnodes = start_end_nodes[0]
endnodes = start_end_nodes[1]
listoflistscontigs = Graph_and_Traversal.startnode(startnodes, graph)

print('edges: ', edges)
print('nodes: ', nodes)
print('graph: ', graph)
print('startnodes: ', startnodes)
print('endnodes: ', endnodes, '\n')


print(Graph_and_Traversal.contigs(listoflistscontigs, endnodes))