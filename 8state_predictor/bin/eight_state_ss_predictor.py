""" This is the structure of the final predictor """

#####################################################
# importing all libraries and scripts
#####################################################

import time
import pickle
import numpy as np
import all_parsing_codes

UNKNOWN = './data/' #here is the place where the query has to be added in fasta

################
# Import model #
################

MODEL_PATH = '../src/' #here is where the trained model is going to be imported
UNPICKLE_MODEL = open(MODEL_PATH, 'rb')
MODEL = pickle.load(UNPICKLE_MODEL)

############################################################################
# Specify the windowsize, must be the same as the trained model since
# if you want to use a different window size, another model must be created
############################################################################

SLIDING_WINDOW = 7

TOPOLOGY_DICT = {1:'G', 2:'I', 3:'H', 4:'E', 5:'B', 6:'T', 7:'S', 8:'C'}
######################################################################
# format: "../results/prediction_results/Name_of_the_result_file.txt
# Specify the path and filename for results, default is the following:
######################################################################

DATE = (time.strftime("%d_%m_%Y"))
RESULT_NAME = ("Prediction_" + DATE + ".txt"")
OUTPUT = open("../results/prediction_results/" + RESULT_NAME, 'w')

############################################################################################
# If you want to use a file that has three lines: ID, seq, topology, but want to leave the
# topology out and receive the predicted topology, use this and comment the other one out
############################################################################################

DICTIONARY = all_parsing_codes.fasta_parser_onlyseq(UNKNOWN)

#################################################################################################
# This takes every sequence in a dicionary one at a time, predicts and then goes to the next one
# saves everything to the output file
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

OUTPUT.close()
print ("Your prediction can be found in ../results/prediction_results/ under the filename" + RESULT_NAME + "!")
