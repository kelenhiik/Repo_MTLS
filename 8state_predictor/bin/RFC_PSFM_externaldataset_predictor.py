""" This predicts topology from an input file using a trained model """
#####################################################
#import my functions from the all_parsing_codes file#
#####################################################

import numpy as np
from sklearn import svm
import pickle
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
import all_parsing_codes

UNKNOWN = '../data/testing_sets/dataset_of_50.txt'
#unknown_fasta = './2protein.fasta'

################
# Import model #
################
MODEL_PATH = '../src/small_models/RFC_PSFM_predictor_109.pkl'
UNPICKLE_MODEL = open(MODEL_PATH, 'rb')
MODEL = pickle.load(UNPICKLE_MODEL)

######################################################################
# Specify the windowsize, must be 7 since I trained my model with it #
######################################################################

SLIDING_WINDOW = 7

TOPOLOGY_DICT = {1:'G', 2:'I', 3:'H', 4:'E', 5:'B', 6:'T', 7:'S', 8:'C'}

#### Specify the path and filename for results, default is the following:

OUTPUT = open("../results/prediction_results/Prediction_external_dataset_PSFM.txt", 'w')

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

DICTIONARY = all_parsing_codes.fasta_parsing_from_3lines(UNKNOWN)
for identification in DICTIONARY:
    pssm_array = all_parsing_codes.pssm_format('../data/PSSM/' + identification + '.fasta.pssm')
    #print(identification)

    sw_of_unknown_topo_pssm = all_parsing_codes.slide_pssm_windows(pssm_array, SLIDING_WINDOW)
    sw_of_unknown_topo_pssm = np.array(sw_of_unknown_topo_pssm)
    prediction = MODEL.predict(sw_of_unknown_topo_pssm)
    prediction_states = prediction.tolist()
    list_of_ss = []

    for number in prediction_states:

        list_of_ss.extend(TOPOLOGY_DICT[number])


    list_in_string = "".join(list_of_ss)

    OUTPUT.write(identification + '\n' + DICTIONARY[identification] + '\n' + list_in_string + '\n')
OUTPUT.close()

