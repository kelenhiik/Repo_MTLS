""" This is the structure of the final predictor using PSFM input"""

#####################################################
# importing all libraries and scripts
#####################################################

import time
import pickle
import gzip
import numpy as np
from bin import all_parsing_codes

#UNKNOWN = './data/PSSM/' #here is the place where the query has to be added in PSSM format
UNKNOWN = './data/PSSM/>D169L.fasta.pssm'
NAME = '>D169L' # Enter the name of the protein, suggested name would be in fasta format ">protname"

################
# Import model #
################

MODEL_PATH = './src/small_models/8SS_RFC_PSFM_predictor_smallmodel.pklz'
#here is where the trained model is going to be imported
UNPICKLE_MODEL = gzip.open(MODEL_PATH, 'rb')
MODEL = pickle.load(UNPICKLE_MODEL)

############################################################################
# Specify the windowsize, must be the same as the trained model since
# if you want to use a different window size, another model must be created
############################################################################

SLIDING_WINDOW = 7

#################### Don't touch the dicitonary ########################
TOPOLOGY_DICT = {1:'G', 2:'I', 3:'H', 4:'E', 5:'B', 6:'T', 7:'S', 8:'C'}
########################################################################
# RESULT_NAME Format: "Name_of_the_result_file.txt"
# Specify the path and filename for results, default is the following:
######################################################################

DATE = (time.strftime("%d_%m_%Y"))
RESULT_NAME = (NAME + "_Prediction_PSFM_" + str(DATE) + ".txt")
OUTPUT = open("./results/prediction_results/" + RESULT_NAME, 'w')

# PS! If you do not change the default name and run the script multiple times
# during one day, the files will be over-written each run.


################################################
# Retrieve the amino acid sequence from the PSSM
################################################

FORMAT_PSSM = (np.genfromtxt(UNKNOWN,
                             skip_header=3,
                             skip_footer=5,
                             autostrip=True,
                             dtype=str,
                             usecols=1))
PSSM_AA_SEQUENCE = "".join(FORMAT_PSSM)



#############################################################
# Formats the PSSM profile into an input for the model.
# Predicts the topology and writes it into the output file
#############################################################

PSSM_ARRAY = all_parsing_codes.pssm_format(UNKNOWN)
SW_OF_ARRAY = all_parsing_codes.slide_pssm_windows(PSSM_ARRAY, SLIDING_WINDOW)
PREDICTION = MODEL.predict(SW_OF_ARRAY)
PREDICTION_STATES = PREDICTION.tolist()
LIST_OF_SS = []

for number in PREDICTION_STATES:

    LIST_OF_SS.extend(TOPOLOGY_DICT[number])

LIST_IN_STRING = "".join(LIST_OF_SS)
OUTPUT.write(NAME + '\n' + PSSM_AA_SEQUENCE + '\n' + LIST_IN_STRING + '\n')
print(NAME + '\n' + PSSM_AA_SEQUENCE + '\n' + LIST_IN_STRING + '\n')
OUTPUT.close()
print("Your prediction can be found in ./results/prediction_results/ under the filename: "
      + RESULT_NAME + "!")
