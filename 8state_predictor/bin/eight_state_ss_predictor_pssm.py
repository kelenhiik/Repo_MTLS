""" This is the structure of the final predictor using PSSM input"""

#####################################################
# importing all libraries and scripts
#####################################################

import time
import pickle
import numpy as np
import all_parsing_codes

UNKNOWN = './data/PSSM/' #here is the place where the query has to be added in PSSM format
NAME = '>protein_name' #enter the name of the protein, suggested name would be in fasta format ">protname"

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
# RESULT_NAME Format: "Name_of_the_result_file.txt"
# Specify the path and filename for results, default is the following:
######################################################################

DATE = (time.strftime("%d_%m_%Y"))
RESULT_NAME = ("Prediction_PSSM_" + DATE + ".txt"")
OUTPUT = open("../results/prediction_results/" + RESULT_NAME, 'w')

################################################
# Retrieve the amino acid sequence from the PSSM
################################################

format_pssm = (np.genfromtxt(filename,
                             skip_header=3,
                             skip_footer=5,
                             autostrip=True,
                             dtype=str,
                             usecols=1))
PSSM_AA_SEQUENCE = "".join(format_pssm)



################################################################################################################
# Formats the PSSM profile into an input for the model. Predicts the topology and writes it into the output file
################################################################################################################

pssm_array = all_parsing_codes.pssm_format(UNKNOWN)
sw_of_unknown_topo_pssm = all_parsing_codes.slide_pssm_windows(pssm_array, SLIDING_WINDOW)
prediction = MODEL.predict(sw_of_unknown_topo_pssm)
prediction_states = prediction.tolist()
list_of_ss = []

for number in prediction_states:

    list_of_ss.extend(TOPOLOGY_DICT[number])

list_in_string = "".join(list_of_ss)
OUTPUT.write(NAME + '\n' + PSSM_AA_SEQUENCE + '\n' + list_in_string + '\n')
OUTPUT.close()
print ("Your prediction can be found in ../results/prediction_results/ under the filename" + RESULT_NAME + "!") 
