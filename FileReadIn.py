'''
Author: Angela Sofia Burkhart Colorado
Date: March 6th, 2022
Purpose: This program opens two files. The first contains a query sequence, which is returned as a string. The second
is a FASTA file containing sequencer reads which are read into a dictionary where the keys are the read information and
the values are the read sequences.
'''

# function takes text file and outputs query sequence as string
def query_sequence(query_file):
    f = open(query_file, "r")
    # for every line in the file
    for line in f:
        #  if the line does not begin with a greater than sign
        if line[0] != '>':
            # query sequence is the line
            query_sequence = line
    # returns query sequence as string
    return query_sequence


# function takes FASTA file and outputs dictionary containing read information as keys and read sequence as values
def reads(reads_file):
    f = open(reads_file, "r")
    reads_dict = {}
    scaffolds = set()
    shortest_read = 0
    for line in f:
        # remove newlines
        line = line.strip()
        # if the line begins with a greater sign
        if line[0] == ">":
            read_info = line[1:]
            scaffolds.add(read_info[:4])
        # else take the read info as key and the line (containing sequence) as value in the dictionary
        else:
            reads_dict[read_info] = line
            # if the shortest read equals 0
            if shortest_read == 0:
                # set shortest_read to length of read sequence
                shortest_read = len(line)
            # if the length of read sequence is shorter than shortest_read
            if len(line) < shortest_read:
                # make current sequence length equal to shortest_read
                shortest_read = len(line)
    # return list containing length of shortest read, set of scaffolds and dictionary of read information (keys) and
    # sequence (values)
    return [shortest_read, scaffolds, reads_dict]



