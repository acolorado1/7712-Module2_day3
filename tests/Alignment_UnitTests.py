'''
Author: Angela Sofia Burkhart Colorado
Date: April 6th, 2022
Purpose: These are the unitests done on the code pertaining to alignment in this project.
'''

import unittest
from src import Alignment


class MyTestCase(unittest.TestCase):

    def test_100percent_alignment(self):
        query_seq = "ATCG"
        contig = ["ATCG"]
        alignment = Alignment.cutoff_percent_test(contig, query_seq)
        self.assertEqual(alignment, {(1, '0:4'): ['ATCG', 0, 4, 1.0]})

    def test_under100percent_alignment(self):
        query_seq = "ATCG"
        contig = ["ATTG"]
        alignment = Alignment.cutoff_percent_test(contig, query_seq)
        self.assertEqual(alignment, {(1, '0:4'): ['ATTG', 0, 4, 0.75]})

    def test_reverse_alignment(self):
        query_seq = "ATCG"
        contig = ["GCTA"]
        alignment = Alignment.cutoff_percent_test(contig, query_seq)
        self.assertEqual(alignment, {(1, '4:0'): ['GCTA', 4, 0, 1.0]})

    def test_no_alignment(self):
        query_seq = "AAAA"
        contig = ["TTTT"]
        alignment = Alignment.cutoff_percent_test(contig, query_seq)
        self.assertEqual(alignment, None)

if __name__ == '__main__':
    unittest.main()
