'''
Author: Angela Sofia Burkhart Colorado
Date: March 6th, 2022
Purpose: This program takes a query sequence and a list of assembled contig sequences and finds all the contigs that
contain the query sequence. Since DNA has errors, and sequencing does as well, alignments will be done with a decreasing
percent cut off starting with 100% percent alignment and decreasing by 0.05 to 50% alignment.
'''

import difflib


# align query sequence to assembled contigs
def alignment(contigs, query, percent_cutoff):
    # initiate dictionary that will contain alignment info
    aligned_contig_info = {}
    # for each contig take each key
    for key in range(len(contigs)):
        # find string contig at key
        contig = contigs[key]
        # keep track of the contig number with counter
        contig_count = key + 1
        # for each index in contig between 0 and the length of the contig minus that of the query
        for startingposition in range(len(contig)-len(query)+1):
            # get endposition of possible alignment site
            end_index = startingposition + len(query)-1
            endingposition = startingposition + len(query)
            # slice contig from index to end position (index plus the length of the query)
            splice = [contigs[key][startingposition:endingposition]]
            # test potential alignment with a predefined cuttoff percentage
            alignment = difflib.get_close_matches(query, splice, n=3, cutoff=percent_cutoff)
            # set variable named forward equal to False
            forward = False
            # if an alignment was found
            if len(alignment) > 0:
                # add contig number and position of alignment as keys and aligned portion of contig, starting position,
                # ending position, and percent cutoff in a list as values
                aligned_contig_info[contig_count, str(startingposition)+":"+str(end_index)] = \
                    [contigs[key], startingposition, end_index, round(percent_cutoff,2)]
                # set forward equal to True
                forward = True
            # if forward is still false check reversed contig splice
            if forward == False:
                # set forward starting position to end position and starting end position to start position
                reverse_starting_pos = end_index
                reverse_ending_pos = startingposition
                # reverse the splice
                reverse_splice = [splice[0][::-1]]
                # perform alignment
                reverse_alignment = difflib.get_close_matches(query, reverse_splice, n=3, cutoff=percent_cutoff)
                # if alignment was found
                if len(reverse_alignment) > 0:
                    # add alignment info to dictionary
                    aligned_contig_info[contig_count, str(reverse_starting_pos)+":"+
                                        str(reverse_ending_pos)] = [contigs[key], reverse_starting_pos,
                                                                    reverse_ending_pos, round(percent_cutoff, 2)]

    return aligned_contig_info


# if no alignments are found with a certain cutoff decrease cutoff percent by 5
def cutoff_percent_test (contigs, query):
    # set cutoff percent to 1.00
    percent_cutoff = 1.00
    # test alignment
    aligned_contig_info = alignment(contigs, query, percent_cutoff)
    # while there is no alignment
    while len(aligned_contig_info) == 0:
        # if percent cutoff is 0.5 or more
        if percent_cutoff >= 0.5:
            # reduce cutoff by 0.05
            percent_cutoff = percent_cutoff - 0.05
            # test alignment with current cut off percent
            aligned_contig_info = alignment(contigs, query, percent_cutoff)
        # if percent cutoff is less that 0.5
        else:
            # no alignments have been found
            return None
    return aligned_contig_info


