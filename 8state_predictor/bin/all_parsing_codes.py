""" Codes necessary for parsing files in FASTA format as inputs for machine learning purposes """
import numpy as np

################################################################################
# This function takes a filename and a sliding window and returns all sequences in binary with
# appropriate sliding windows. The format for SVM predicting?
################################################################################


def parse_unknown_file(filename, sliding_window):
    """ Parses an unknown file which only has an ID and sequence """

    all_unknown_topo_seq_set = []
    id_seq = []
    seq_of_query = []
    dictionary = fasta_parser_onlyseq(filename)

    for identification in dictionary:
        sw_of_unknown_topo_seq = encode_protein((dictionary[identification]), sliding_window)

#in the end, if i want one protein at a time, this is the place I call my model to predict
#the thing I have here, the previous line. Maybe I even have to write a new function for this




        all_unknown_topo_seq_set.extend(sw_of_unknown_topo_seq)
        id_seq.append(identification)
        seq_of_query.append(dictionary[identification])


    id_seq1 = "".join(id_seq)
    seq_of_query1 = "".join(seq_of_query)
    all_unknown_topo_seq_set = np.array(all_unknown_topo_seq_set)
    return all_unknown_topo_seq_set, id_seq1, seq_of_query1


################################################################################
# Takes a fasta file and sliding windows. The outputs are pssm feature array and
# topology array, but in sets of 70% for train and 30% for test.
################################################################################


def protein_w_pssm_train(filename, sliding_window):
    """ Input for SVM for protein and it's PSSM: 70% training, 30% testing """

    pssm_training_set = []
    train_topologies = []

    pssm_test_set = []
    test_topologies = []

    dictionary = fasta_parser(filename)

    sorted_keys = sorted(dictionary.keys(), key=lambda x: x[3:])
    keys_train = sorted_keys[:int(0.7 * len(dictionary))]

    # Train set:
    for identification in keys_train:
        pssm_array = pssm_format('../data/PSSM/' + identification + '.fasta.pssm')
        pssm_feature_set = slide_pssm_windows(pssm_array, sliding_window)
        pssm_training_set.extend(pssm_feature_set)
        topology_set = topology_in_numbers((dictionary[identification])[1])
        train_topologies.extend(topology_set)

    # Test set:
    for identification in set(dictionary) - set(keys_train):
        pssm_array = pssm_format('../data/PSSM/' + identification + '.fasta.pssm')
        pssm_feature_set = slide_pssm_windows(pssm_array, sliding_window)
        pssm_test_set.extend(pssm_feature_set)
        topology_set = topology_in_numbers((dictionary[identification])[1])
        test_topologies.extend(topology_set)

    pssm_training_set = np.array(pssm_training_set)
    train_topologies = np.array(train_topologies)
    pssm_test_set = np.array(pssm_test_set)
    test_topologies = np.array(test_topologies)

    return pssm_training_set, train_topologies, pssm_test_set, test_topologies


################################################################################
# Takes a fasta file and sliding windows. The outputs are pssm feature array and
# topology array
################################################################################


def pssm_svm(filename, sliding_window):
    """ Creates SVM training inputs """
    dictionary = fasta_parser(filename)
    all_pssm = []
    pssm_topologies = []
    sorted_keys = sorted(dictionary.keys(), key=lambda x: x[3:])
    for identification in sorted_keys:
        pssm_array = pssm_format('../data/PSSM/' + identification + '.fasta.pssm')
        feature_set = slide_pssm_windows(pssm_array, sliding_window)
        all_pssm.extend(feature_set)
        topology_set = topology_in_numbers((dictionary[identification])[1])
        pssm_topologies.extend(topology_set)
        #print (topology_set)
        #print (identification)
    #print(pssm_topologies)

    all_pssm = np.array(all_pssm)
    pssm_topologies = np.array(pssm_topologies)
    return all_pssm, pssm_topologies


################################################################################
# Takes a 1D numpy array and creates sliding window features
################################################################################


def slide_pssm_windows(pssm_array, sliding_window):
    """ Takes in an array format pssm and creates sliding window features """
    pssm_set = []
    pad = int(sliding_window//2)
    for i in range(len(pssm_array)):
        #print (i)
        if i < pad:
            number_of_pads = pad-i
            temp_encoded_window = [0]*(20*number_of_pads)
            for lists in pssm_array[:i+pad+1]:
                #print (lists) works
                temp_encoded_window.extend(lists)  # Extend (not append)
            pssm_set.append(temp_encoded_window) # Save to pssm training set

        elif i > (len(pssm_array)-pad-1):
            #print(i)
            number_of_pads = pad - (len(pssm_array)- 1 - i)
            temp_encoded_window = []
            for lists in pssm_array[i-pad:]:
                temp_encoded_window.extend(lists)  # Extend (not append)
            temp_encoded_window.extend([0]*(20*number_of_pads))
            pssm_set.append(temp_encoded_window) # Save to pssm training set

        else:
            temp_window = pssm_array[i-pad:i+pad+1] # Extract sliding window
            temp_encoded_window = []
            for lists in temp_window:       # Go through each pssm list in sliding window
                temp_encoded_window.extend(lists)  # Extend (not append)
                #print(temp_encoded_window)
            pssm_set.append(temp_encoded_window) # Save to training set

    return pssm_set

################################################################################
# Takes a file that is in a PSSM profile format and returns necessary lines in
# SVM format
################################################################################


def pssm_format(filename):
    """ PSSM into array format """
    format_pssm = (np.genfromtxt(filename,
                                 skip_header=3,
                                 skip_footer=5,
                                 autostrip=True,
                                 usecols=range(22, 42)))/100

    return format_pssm


################################################################################
# This function takes a filename and a sliding window and returns all sequences in binary with
# appropriate sliding windows. The format for SVM training.
################################################################################


def parse_with_all_codes(filename, sliding_window):
    """ Parses the three line txt file and also sorts the headings for easier splitting later """

    all_training_set = []
    all_topologies = []
    dictionary = fasta_parser(filename)
    # get the keys in the same order, since if i wanna cross-validate, I'd have the same one's
    # when checking dif parameters
    sorted_keys = sorted(dictionary.keys(), key=lambda x: x[3:])

    for identification in sorted_keys:
        training_set = encode_protein((dictionary[identification][0]), sliding_window)
        all_training_set.extend(training_set)
        topology_set = topology_in_numbers((dictionary[identification])[1])
        all_topologies.extend(topology_set)

    all_topologies = np.array(all_topologies)
    all_training_set = np.array(all_training_set)
    return all_training_set, all_topologies


################################################################################
# This function takes a filename and a sliding window.
# Then it calls the parser function and makes a dictionary out of the filename.
# Afterwards it splits the dictionary keys so I could have a separate training and testing set.
# Complicated with a dictionary, bias is minimized by sorting the dictionary
# keys by the positions in the name of the key that have been assigned randomly in pdb.
# The out of this key list it takes 70% for training and results in 30% for
# testing sets that it encodes for proteins and topology using custom functions,
# returns results as numpy arrays.
################################################################################


def parse_with_train_test(filename, sliding_window):
    """ Parses the 3line file to 70% and 30% for training and testing """

    all_training_set = []
    train_topologies = []

    all_test_set = []
    test_topologies = []

    dictionary = fasta_parser(filename)

    # EXPLAIN IN A COMMENT:
    # sorts keys in my dictionary based on the values from 3:end and saves them in a variable
    # sorted_keys so I can specify from that list the 70% i wanna use for testing. lambda is a
    # small function, so insead of defining a function (x) you put lambda.

    sorted_keys = sorted(dictionary.keys(), key=lambda x: x[3:])
    keys_train = sorted_keys[:int(0.7 * len(dictionary))]

    # Train set:
    for identification in keys_train:
        training_set = encode_protein((dictionary[identification][0]), sliding_window)
        all_training_set.extend(training_set)
        topology_set = topology_in_numbers((dictionary[identification])[1])
        train_topologies.extend(topology_set)

    # Test set:
    for identification in set(dictionary) - set(keys_train):
        test_set = encode_protein((dictionary[identification][0]), sliding_window)
        all_test_set.extend(test_set)
        topology_set = topology_in_numbers((dictionary[identification])[1])
        test_topologies.extend(topology_set)

    all_training_set = np.array(all_training_set)
    train_topologies = np.array(train_topologies)
    all_test_set = np.array(all_test_set)
    test_topologies = np.array(test_topologies)

    return all_training_set, train_topologies, all_test_set, test_topologies


################################################################################
# Takes a file with ID, seq, topology and assigns ID as key, seq and topology as values.
################################################################################
from re import sub

def fasta_parser(filename):
    """ This creates a dictionary of a 3line txt file """

    list1 = [line.rstrip() for line in (open(filename, 'r')) if len(line.strip()) != 0]
    ID_list = []
    sequence_list = []
    topology_list = []
    for line in list1[::3]:
        ID_list.append(line.upper())
    for line in list1[1::3]:
        lines = sub("[a-z]",'C',line)
        sequence_list.append(lines.upper())
    for line in list1[2::3]:
        topology_list.append(line.upper())

    dict1 = dict(zip(ID_list, zip(sequence_list, topology_list)))
    return dict1


def fasta_parser_onlyseq(filename):
    """ Parses a file with only ID and sequence in two lines """
    list1 = [line.rstrip() for line in (open(filename, 'r')) if len(line.strip()) != 0]
    ID_list = []
    sequence_list = []
    for line in list1[::2]:
        ID_list.append(line.upper())
    for line in list1[1::2]:
        lines = sub("[a-z]",'C',line)
        sequence_list.append(lines.upper())


    dict2 = dict(zip(ID_list, sequence_list))
    return dict2


def fasta_parsing_from_3lines(filename):
    """ Takes a file with three lines: ID, seq, topo. Output dictionary ID:(sequence) """
    list1 = [line.rstrip() for line in (open(filename, 'r')) if len(line.strip()) != 0]
    ID_list = []
    sequence_list = []
    for line in list1[::3]:
        ID_list.append(line.upper())
    for line in list1[1::3]:
        lines = sub("[a-z]",'C',line)
        sequence_list.append(lines.upper())
    dict3 = dict(zip(ID_list, sequence_list))
    return dict3

################################################################################
# Manually made dictionary for the topologies in numerical form
################################################################################


TOPOLOGY_DICT = {'G':1, 'I':2, 'H':3, 'E':4, 'B':5, 'T':6, 'S':7, 'C':8}


################################################################################
# Create a binary dict for the aa residues and specify what to do with uncommon residues
################################################################################


AMINO_ACID_DICT = {}
AMINOACIDS = 'GALMFWKQESPVICYHRNDT'

for aa in AMINOACIDS:
    TEMP_VECTOR = [0]*20

    TEMP_VECTOR[AMINOACIDS.index(aa)] = 1
    AMINO_ACID_DICT[aa] = TEMP_VECTOR

AMINO_ACID_DICT['X'] = [1/20] * 20
TEMP_VECTOR = [0]*20
TEMP_VECTOR[AMINOACIDS.index('Q')] = 0.5
TEMP_VECTOR[AMINOACIDS.index('E')] = 0.5
AMINO_ACID_DICT['Z'] = TEMP_VECTOR
TEMP_VECTOR = [0]*20
TEMP_VECTOR[AMINOACIDS.index('N')] = 0.5
TEMP_VECTOR[AMINOACIDS.index('D')] = 0.5
AMINO_ACID_DICT['B'] = TEMP_VECTOR
TEMP_VECTOR = [0]*20
TEMP_VECTOR[AMINOACIDS.index('I')] = 0.5
TEMP_VECTOR[AMINOACIDS.index('L')] = 0.5
AMINO_ACID_DICT['J'] = TEMP_VECTOR

# DECIDE WHAT TO DO WITH THESE:
AMINO_ACID_DICT['O'] = AMINO_ACID_DICT['S']
AMINO_ACID_DICT['U'] = AMINO_ACID_DICT['S']


################################################################################
# Go through a sequence and do all full sliding windows#
################################################################################


def encode_protein(seq, windowlength):
    """ This encodes any sequence to sliding windows, all binary """

    training_set = []
    pad = int(windowlength//2)
    for i in range(len(seq)): # All full windows
        if i < pad:

            number_of_pads = pad-i
            temp_encoded_window = [0]*(20*number_of_pads)
            for positions in seq[:i+pad+1]:       # Go through each AA in sliding window
                temp_encoded_window.extend(AMINO_ACID_DICT[positions])  # Extend (not append)
            training_set.append(temp_encoded_window) # Save to training set
        elif i > (len(seq)-pad-1):
            #print(i)
            number_of_pads = pad - (len(seq)- 1 - i)
            temp_encoded_window = [] #[0]*(20*number_of_pads)
            for positions in seq[i-pad:]:       # Go through each AA in sliding window
                temp_encoded_window.extend(AMINO_ACID_DICT[positions])  # Extend (not append)
            temp_encoded_window.extend([0]*(20*number_of_pads))
            training_set.append(temp_encoded_window) # Save to training set
        else:
            temp_window = seq[i-pad:i+pad+1] # Extract sliding window
            temp_encoded_window = []
            for positions in temp_window:       # Go through each AA in sliding window
                temp_encoded_window.extend(AMINO_ACID_DICT[positions])  # Extend (not append)
            # print(temp_encoded_window)
            training_set.append(temp_encoded_window) # Save to training set
    return training_set


################################################################################
# Fix topologies #
################################################################################


def topology_in_numbers(my_topo):
    """ Translates the topology to the right format"""

    topologies = []
    for topology in my_topo:

        topologies.append(TOPOLOGY_DICT[topology])

    return topologies

if __name__ == "__main__":
    #print(parse_with_all_codes("dssp_8_state.3line.txt", 3))
    #print(fasta_parser_onlyseq('250_270_set.3line.txt'))
    print(fasta_parsing_from_3lines("../data/training_sets/twoseq.txt"))
