""" This predicts topology from an input file using a RFC PSFM trained model, the input is a fasta file,
where all the proteins must have a PSSM-profile in the designated folder """
#####################################################
#import my functions from the all_parsing_codes file#
#####################################################

import numpy as np
import pickle
import gzip
from bin import all_parsing_codes


#################################################################################
# Input file, which is a fasta file. All the proteins must have a PSSM profile in
# the designated folder with a >PROTNAME.fasta.pssm name. >D169L.fasta.pssm
#################################################################################
UNKNOWN = './data/testing_sets/dataset_of_50.txt'


################
# Import model #
################

MODEL_PATH = './src/small_models/8SS_RFC_PSFM_predictor_smallmodel.pklz'
UNPICKLE_MODEL = gzip.open(MODEL_PATH, 'rb')
MODEL = pickle.load(UNPICKLE_MODEL)

######################################################################
# Specify the windowsize, must be 7 since I trained my model with it.
# Unless you import another PSFM trained model, don't change it.
######################################################################

SLIDING_WINDOW = 7

#################### Don't touch the dicitonary ########################
TOPOLOGY_DICT = {1:'G', 2:'I', 3:'H', 4:'E', 5:'B', 6:'T', 7:'S', 8:'C'}
########################################################################
# Specify the path and filename for results, since this script is meant
# to run on the provided external dataset the default is the following:
########################################################################

OUTPUT = open("./results/prediction_results/PSFM_Prediction_external_dataset.txt", 'w')

############################################################################################
# If you want to use a file that has three lines: ID, seq, topology, but only use the
# ID of the protein for PSFM recognition, use this and comment the other one out
############################################################################################

DICTIONARY = all_parsing_codes.fasta_parsing_from_3lines(UNKNOWN)

#################################################################################################
# If you want to use a file that has two lines: ID, seq. OR any fasta file with the same format,
# use this for the same purpose and comment the above one out
#################################################################################################

#DICTIONARY = all_parsing_codes.fasta_parser_onlyseq(unknown_fasta)

##################################################################################################
# This takes every ID and searches the PSSM folder for such files, if the files were retrieved using
# pdb.py and dssp.sh somewhere in the bin directory, should be fine
##################################################################################################

for identification in DICTIONARY:
    pssm_array = all_parsing_codes.pssm_format('./data/PSSM/' + identification + '.fasta.pssm')

    sw_of_unknown_topo_pssm = all_parsing_codes.slide_pssm_windows(pssm_array, SLIDING_WINDOW)
    sw_of_unknown_topo_pssm = np.array(sw_of_unknown_topo_pssm)
    prediction = MODEL.predict(sw_of_unknown_topo_pssm)
    prediction_states = prediction.tolist()
    list_of_ss = []

    for number in prediction_states:

        list_of_ss.extend(TOPOLOGY_DICT[number])


    list_in_string = "".join(list_of_ss)

    OUTPUT.write(identification + '\n' + DICTIONARY[identification] + '\n' + list_in_string + '\n')
    print(identification + '\n' + DICTIONARY[identification] + '\n' + list_in_string + '\n')
OUTPUT.close()
print ("Your prediction can be found in ./results/prediction_results/ under the filename: " + "PSFM_Prediction_external_dataset.txt" + "!")
