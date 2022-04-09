'''
Author: Angela Sofia Burkhart Colorado
Date: March 6th, 2022
Purpose: This program takes assembled contigs that were aligned to query sequence and writes two files. The first will
only contain the sequence of the largest assembled contig containing the query sequence. The second file will contain
contig info including the name of the reads that were used to assemble the contig, the name of the contig, starting and
ending coordinates in the sequencing read that matched with the query, and the starting and ending coordinates of the
contig that matched with the query sequence.
'''


# creates first output file with largest contig containing query sequence
def largest_contig(alignment_info, scaffolds):
    # for each scaffold
    largest_length_info = {}
    for scaffold in scaffolds:
        # initialize length of largest contig
        length_largest_contig = 0
        # for each contig
        for contig in alignment_info:
            # if the scaffold information equals the current scaffold
            if contig[:5]==scaffold:
                # for each alignment per contig
                for alignment in alignment_info[contig]:
                    # find length of current contig
                    length_contig = len(alignment_info[contig][alignment][0])
                    # if the length of current contig larger than any previous contigs
                    if length_contig > length_largest_contig:
                        # make length of current contig equal to the largest length
                        length_largest_contig = length_contig
        for contig in alignment_info:
            # if the scaffold information equals the current scaffold
            if contig[:5]==scaffold:
                # for each alignment per contig
                for alignment in alignment_info[contig]:
                    # find length of current contig
                    length_contig = len(alignment_info[contig][alignment][0])
                    # if the length of current contig equal to the largest contig found
                    if length_contig == length_largest_contig:
                        # add contig information to dictionary with the format {(scaffod, contig number): sequence}
                        scaffold = contig[:5]
                        contig_num = contig[6:]
                        sequence = alignment_info[contig][alignment][0]
                        largest_length_info[(scaffold, contig_num)] = sequence


    # open a file where the largest contigs will be written into
    f = open("../ALLELES.fasta", "w")
    # for every key in the largest aligned contigs dictionary
    for key in largest_length_info:
        # get the scaffold information from the key
        scaffold = str(key[0])
        # get the contig number from the scaffold information
        contig_num = str(key[1])
        # write a line containing scaffold and contig information followed by a line with the sequence
        f.write(">"+scaffold +": contig"+contig_num + "\n"+largest_length_info[key] + "\n")
    f.close()
    return largest_length_info


# creates output file containing alignment information of the largest aligned contigs
def contig_information(contig_info, alignment_info, largest_contig_info,k):
    # intialize dictionary containing alignment information
    line_info = {}
    # initialize counter variable which will serve as keys to the dictionary
    count = 1
    # for key in largest aligned contig dictionary, key format: ('scaffold', contig number)
    for key in largest_contig_info:
        # get scaffold
        scaffold = key[0]
        # get contig number
        contig_num = key[1]
        # for each scaffold and contig get key
        alignment_key = scaffold+":"+str(contig_num)
        contig_alignment_info = alignment_info[alignment_key]
        print(contig_alignment_info)
        for key in contig_alignment_info:
            # get start position in contig where query aligned to contig
            contig_start_position = contig_alignment_info[key][1]
            # get end position in contig where query aligned to contig
            contig_end_position = contig_alignment_info[key][2]
            # get the percent cutoff that qas used when perfoming alignment
            contig_percent_cutoff = contig_alignment_info[key][3]
            # get path of nodes traveled to create contig
            path = contig_info[scaffold]["paths"][int(contig_num)]
            # to get the corresponding starting position in the read where the query aligned to take contig position
            # if contig start position is less than or equal to k-2
            if contig_start_position <= k-2:
                # the first node in the path will contain read position information
                start_node = path[0]
                # grab the FASTA ID of the read from the first position
                readID = start_node.ID
                # read starting position will equal contig starting position
                read_start_position = contig_start_position
            # if the contig start position is greater than or equal to 3
            else:
                # find node corresponding to contig position (2 indexes lower than contig position)
                find_node = k-2
                # get the node whose ending position will equal the reads ending position
                start_node = path[contig_start_position-find_node]
                # find node FASTA ID
                readID = start_node.ID
                # get the node ending position (attribute of class)
                read_start_position = start_node.e

            # if contig ending position is k minus 2 read and contig ending positions are the same
            if contig_end_position <= k-2:
                read_end_position = contig_end_position
            else:
                # get node where end position (class attribute) will be read end position and assign to variable
                find_node = k - 2
                end_node = path[contig_end_position-find_node]
                read_end_position = end_node.e

            # add to dictionary counter (key) and readID, contig number, read start position, read end position, contig
            # start position, contig end position, and percent cutoff of alignment as a list (value)
            line_info[count] = [readID, "contig"+str(contig_num), str(read_start_position), str(read_end_position),
                                str(contig_start_position), str(contig_end_position), str(contig_percent_cutoff)]
            # increase counter
            count += 1

    # open file where alignment info will be written into
    f = open("../ALLELES.aln", "w")
    # write header information
    f.write("sseqid \t qseqid \t sstart \t send \t qstart \t qend \t pcutoff\n")
    # for every key value pair in line info dictionary
    for key in line_info:
        # write information into the file
        list_info = line_info[key]
        f.write(list_info[0]+" \t "+list_info[1]+" \t "+list_info[2]+" \t "+list_info[3]+" \t "+list_info[4]+" \t "+
                list_info[5]+" \t "+list_info[6]+"\n")
    f.close()
    return