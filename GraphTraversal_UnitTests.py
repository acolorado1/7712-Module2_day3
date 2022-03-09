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
        self.assertEqual(kmers, ['MYDO','YDOG','DOGM','OGMA','GMAX'])

    def test_GraphTraversal(self):
        example_adjacency_list = {'MYD': ['YDO'], 'YDO': ['DOG'], 'DOG': ['OGM'],'OGM': ['GMA'], 'GMA': ['MAX'],
                                  'MAX': []}
        graph = GT.graph_traversal(example_adjacency_list, 'OGM')
        self.assertEqual(graph, ['OGM','GMA','MAX'])

    def test_InfiniteLoops(self):
        example_adjacency_list = {'MYD': ['YDO'], 'YDO': ['DOG'], 'DOG': ['OGM'], 'OGM': ['GMA'], 'GMA': ['MAX'],
                                  'MAX': ['MYD']}
        graph = GT.graph_traversal(example_adjacency_list, 'MYD')
        self.assertEqual(graph, ['MYD','YDO','DOG','OGM','GMA','MAX'])

    def test_traversal_with_dectable_startnodes(self):
        nodes = [('MYD', 'YDO'),('YDO','DOG'),('DOG','OGM'),('OGM','GMA'),('GMA','MAX')]
        example_adjacency_list = {'MYD': ['YDO'], 'YDO': ['DOG'], 'DOG': ['OGM'], 'OGM': ['GMA'], 'GMA': ['MAX'],
                                  'MAX': ['MYD']}
        startnodes_endnodes = GT.list_startnodes_endnodes(nodes)
        startnodes = startnodes_endnodes[0]
        listoflistscontigs = GT.startnode(startnodes, example_adjacency_list)
        self.assertEqual(listoflistscontigs, [['MYD','YDO','DOG','OGM','GMA','MAX']])

if __name__ == '__main__':
    unittest.main()
