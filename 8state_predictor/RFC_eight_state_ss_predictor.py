""" This is the final 8-state secondary structure from protein amino acid sequence predictor """

#####################################################
# Importing all libraries and scripts
#####################################################

import time
import pickle
import gzip
import numpy as np
from bin import all_parsing_codes

################################################################################
# UNKNOWN = './data/' #here is the place where the query has to be added in fasta
################################################################################

UNKNOWN = './data/testing_sets/dataset_of_50.txt'

##############################################################
# Import model, MODEL_PATH = '../src/' etc.
# here is where the trained model is going to be imported from
##############################################################

MODEL_PATH = './src/small_models/8SS_RFC_sequence_predictor_smallmodel.pklz'
UNPICKLE_MODEL = gzip.open(MODEL_PATH, 'rb')
MODEL = pickle.load(UNPICKLE_MODEL)

############################################################################
# Specify the windowsize, must be the same as the trained model.
# if you want to use a different window size, another model must be created
############################################################################

SLIDING_WINDOW = 11

#################### Don't touch the dicitonary ########################
TOPOLOGY_DICT = {1:'G', 2:'I', 3:'H', 4:'E', 5:'B', 6:'T', 7:'S', 8:'C'}
########################################################################
# Specify the path and filename for results format:
# "../results/prediction_results/Name_of_the_result_file.txt"
# Default is the following resulting in the today's date:
########################################################################

DATE = (time.strftime("%d_%m_%Y"))
RESULT_NAME = ("Prediction_" + str(DATE) + ".txt")
OUTPUT = open("./results/prediction_results/" + RESULT_NAME, 'w')

# PS! If you do not change the default name and run the script multiple times
# during one day, the files will be over-written each run.

###########################################################################################
# If you want to use a file that has three lines: ID, seq, topology, but want to leave the
# topology out and receive the newly predicted topology, use "parsing _from_3lines" and
# comment the other one out. fasta_parser_onlyseq parses a two lined file: ID, sequence
###########################################################################################

DICTIONARY = all_parsing_codes.fasta_parsing_from_3lines(UNKNOWN)

#DICTIONARY = all_parsing_codes.fasta_parser_onlyseq(UNKNOWN)

#################################################################################################
# This takes every sequence in a dicionary one at a time, predicts and then goes to the next one
# saves everything to the output file and prints it on the terminal screen.
#################################################################################################

for identification in DICTIONARY:

    sw_of_unknown_topo_seq = all_parsing_codes.encode_protein((DICTIONARY[identification]),
                                                              SLIDING_WINDOW)
    sw_of_unknown_topo_seq = np.array(sw_of_unknown_topo_seq)
    prediction = MODEL.predict(sw_of_unknown_topo_seq)
    prediction_states = prediction.tolist()
    list_of_ss = []

    for number in prediction_states:

        list_of_ss.extend(TOPOLOGY_DICT[number])


    list_in_string = "".join(list_of_ss)

# it also prints it on the terminal screen

    OUTPUT.write(identification + '\n' + DICTIONARY[identification] + '\n' + list_in_string + '\n')
    print(identification + '\n' + DICTIONARY[identification] + '\n' + list_in_string + '\n')
OUTPUT.close()
print ("Your prediction can be found in ./results/prediction_results/ under the filename: " + RESULT_NAME + "!")
