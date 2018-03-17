""" This predicts protein sequence topology from an input file using a trained RFC model """
#######################################################
# Import my functions from the all_parsing_codes file #
#######################################################

import numpy as np
import pickle
import gzip
import all_parsing_codes

##############################################################
# The fasta file of proteins for which topology is predicted #
##############################################################

UNKNOWN = '../data/testing_sets/dataset_of_50.txt'

################################################################
# Import model trained on 11 sequences for size considerations #
# This can be changed to specify the path to any created model #
################################################################

MODEL_PATH = '../src/small_models/8SS_RFC_sequence_predictor_smallmodel.pklz'
UNPICKLED_MODEL = gzip.open(MODEL_PATH, 'rb')
MODEL = pickle.load(UNPICKLED_MODEL)

##################################################
# Window size for this assignment is 11
# Otherwise, enter the windowsize which has
# to be the same that was used for model training
##################################################

SLIDING_WINDOW = 11

###########################################
# For topology value mapping, don't touch #
###########################################

TOPOLOGY_DICT = {1:'G', 2:'I', 3:'H', 4:'E', 5:'B', 6:'T', 7:'S', 8:'C'}

##############################################################################
#### Specify the path and filename for results, default is the following:
##############################################################################
output = open("../results/prediction_results/Prediction_external_dataset_seqs_smallmodel.txt", 'w')

############################################################################################
# If you want to use a file that has three lines: ID, seq, topology, but want to leave the
# topology out and receive the predicted topology, use this and comment the other one out
############################################################################################

dictionary = all_parsing_codes.fasta_parsing_from_3lines(UNKNOWN)

#################################################################################################
# If you want to use a file that has two lines: ID, seq. OR any fasta file with the same format,#
# use this and comment the above one out
#################################################################################################

#dictionary = all_parsing_codes.fasta_parser_onlyseq(unknown_fasta)

##################################################################################################
# This takes every sequence in a dicionary one at a time, predicts and then goes to the next one,#
#also creates a file for it #
##################################################################################################

for identification in dictionary:


    sw_of_unknown_topo_seq = all_parsing_codes.encode_protein((dictionary[identification]), SLIDING_WINDOW)
    sw_of_unknown_topo_seq = np.array(sw_of_unknown_topo_seq)
    prediction = MODEL.predict(sw_of_unknown_topo_seq)
    prediction_states = prediction.tolist()
    list_of_ss = []

    for number in prediction_states:

        list_of_ss.extend(TOPOLOGY_DICT[number])


    list_in_string = "".join(list_of_ss)

# it also prints it on the terminal screen

    output.write(identification + '\n' + dictionary[identification] + '\n' + list_in_string + '\n')
    print(identification + '\n' + dictionary[identification] + '\n' + list_in_string + '\n')
output.close()
