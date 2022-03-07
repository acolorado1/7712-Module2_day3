'''
Author: Angela Sofia Burkhart Colorado
Date: March 6th, 2022
Purpose: This program takes a query sequence and a list of assembled contig sequences and finds all the contigs that
contain the query sequence. Since DNA has errors, and sequencing does as well, the query sequence will only have to
align to the contig with 95% (check the rate of errors) fidelity.
'''

# TODO
def alignment(contigs, query):
    # for each contig
        # walk along the sequence
        # find region that matches query with only under 5% error (check this percentage)
    return None

def reverse_alignment(contigs, query):
    # for each contig
        # flip the contig to get the reverse strand
        # walk along sequence
        # find region where query sequence aligns with the reversed contig
    return None