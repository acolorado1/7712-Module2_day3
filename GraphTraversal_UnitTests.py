'''
Author: Angela Sofia Burkhart Colorado
Date: March 8th, 2022
Purpose: Perform unit tests on functions pertaining to the graph traversal portion of this project.
'''

import unittest
import Graph_and_Traversal as GT

class TestGraph_and_Traversal(unittest.TestCase):
    def test_kmers(self):
        example_read = {1: "MYDOGMAX"}
        # set largest sequence variable to arbitrary number
        kmers = GT.kmers(example_read, 4, 5)
        kmer_list = []
        for edge in kmers:
            kmer_list.append(edge.seq)
        self.assertEqual(kmer_list, ['MYDO','YDOG','DOGM','OGMA','GMAX'])

    def test_startnode_detection(self):
        example_reads = {1: "MYDOGMAX", 2: "MYDOGSMOKEY"}
        kmers = GT.kmers(example_reads,4,5)
        nodes = GT.k_1mers(kmers)
        start_end = GT.startnodes_endnodes(nodes)
        startnodes = start_end["startnodes"]
        startnode_list = set()
        for node in startnodes:
            startnode_list.add(node.seq)
        self.assertEqual(startnode_list, {"MYD"})

    def test_endnode_detection(self):
        example_reads = {1: "MYDOGMAX", 2: "MYDOGSMOKEY"}
        kmers = GT.kmers(example_reads, 4, 5)
        nodes = GT.k_1mers(kmers)
        start_end = GT.startnodes_endnodes(nodes)
        endnodes = start_end["endnodes"]
        endnode_list = set()
        for node in endnodes:
            endnode_list.add(node.seq)
        self.assertEqual(endnode_list, {"MAX","KEY"})

    def test_forward_GraphTraversal(self):
        example_adjacency_list = {'MYD': ['YDO'], 'YDO': ['DOG'], 'DOG': ['OGM'], 'GMA': ['MAX'], 'MAX': [],
                                  'OGM': ['GMA']}
        startnodes = 'MYD'
        graph = GT.graph_traversal(example_adjacency_list, startnodes, start=True)
        self.assertEqual(graph, ['MYD','YDO','DOG','OGM','GMA','MAX'])

    def test_reverse_GraphTraversal(self):
        example_adjacency_list = {'MYD': [], 'YDO': ['MYD'], 'DOG': ['YDO'], 'GSM': ['OGS'], 'SMO': ['GSM'],
                                  'MOK': ['SMO'], 'GMA': ['OGM'], 'MAX': ['GMA'], 'OGM': ['DOG'], 'OKE': ['MOK'],
                                  'OGS': ['DOG'], 'KEY': ['OKE']}
        graph = GT.graph_traversal(example_adjacency_list, 'MAX', start=False)
        self.assertEqual(graph, ['MYD','YDO','DOG','OGM','GMA','MAX'])

    def test_InfiniteLoops(self):
        example_adjacency_list = {'MYD': ['YDO'], 'YDO': ['DOG'], 'DOG': ['OGM'], 'OGM': ['GMA'], 'GMA': ['MAX'],
                                  'MAX': ['MYD']}
        graph = GT.graph_traversal(example_adjacency_list, 'MYD', start=True)
        self.assertEqual(graph, ['MYD','YDO','DOG','OGM','GMA','MAX'])



if __name__ == '__main__':
    unittest.main()
