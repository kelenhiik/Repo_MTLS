""" This script trains a model using Random forests and predicts
    the 8 state secondary structure from the amino acid sequence of a protein"""

import pickle
import gzip
import numpy as np
from sklearn.ensemble import RandomForestClassifier as RFC
from bin import all_parsing_codes

################################################################################
# Enter the path to your training set, which has to be in a 3-line format:
# 1st: Protein ID, 2nd: Amino acid sequence, 3d: Topology
# Used in the project: './data/train_test_sets/randomized109_proteins.3line.txt'
################################################################################

TEMPFILE = './data/train_test_sets/randomized109_proteins.3line.txt'

#################################################################################
# Enter parameter values you wish to change. Default parameteres are the best for
# 3-fold cross-validation score: window = 11, estimators = 350, min splits = 3
# that are used in the project
#################################################################################
SLIDING_WINDOW = 11
N_ESTIMATORS = 350
MIN_SAMPLES_SPLIT = 3

###########################################################################
# Retrieve your training information, this is going to parse a whole file #
###########################################################################
X_TRAIN, Y_TRAIN = all_parsing_codes.parse_with_all_codes(TEMPFILE, SLIDING_WINDOW)

#######################################################
# Create a model with the before-mentioned parameters #
#######################################################

RFC_PREDICTOR_MODEL = RFC(n_estimators=N_ESTIMATORS,
                          min_samples_split=MIN_SAMPLES_SPLIT,
                          n_jobs=-1)

RFC_PREDICTOR_MODEL.fit(X_TRAIN, Y_TRAIN)

################################################################
# Save the model for future usage
# Saved model path used in the project:
# './src/small_models/8SS_RFC_sequence_predictor_109model.pklz'
################################################################
LOCATION = './src/small_models/8SS_RFC_sequence_predictor_109model.pklz'
OUT_LOCATION = gzip.open(LOCATION, 'wb')
pickle.dump(RFC_PREDICTOR_MODEL, OUT_LOCATION, protocol=pickle.HIGHEST_PROTOCOL)
OUT_LOCATION.close()

############################################################
# The fasta file of proteins for which topology is predicted
# The dataset used in the project, retrieved from PDB:
# './data/testing_sets/dataset_of_50.txt'
############################################################

UNKNOWN = './data/testing_sets/dataset_of_50.txt'


################################################################
# Import the previously created model. Path used in the project:
# './src/small_models/8SS_RFC_sequence_predictor_109model.pklz'
################################################################

MODEL_PATH = './src/small_models/8SS_RFC_sequence_predictor_109model.pklz'
UNPICKLED_MODEL = gzip.open(MODEL_PATH, 'rb')
MODEL = pickle.load(UNPICKLED_MODEL)

#################### Don't touch the dicitonary ###########################
TOPOLOGY_DICT = {1:'G', 2:'I', 3:'H', 4:'E', 5:'B', 6:'T', 7:'S', 8:'C'}
###########################################################################
# Specify the path and filename for results, used in the project:
# "./results/prediction_results/Prediction_from_external_dataset_seqs.txt"
###########################################################################
OUTPUT = open("./results/prediction_results/Prediction_from_external_dataset_seqs.txt", 'w')

############################################################################################
# If you want to use a file that has three lines: ID, seq, topology, but want to leave the
# topology out and receive the predicted topology, use this and comment the other one out
# This one is used in the project
############################################################################################

DICTIONARY = all_parsing_codes.fasta_parsing_from_3lines(UNKNOWN)

#################################################################################################
# If you want to use a file that has two lines: ID, seq. OR any fasta file with the same format,
# use this and comment the above one out
#################################################################################################

#DICTIONARY = all_parsing_codes.fasta_parser_onlyseq(unknown_fasta)

###########################################################
# Predicts the topology and writes it to the specified path
# Also prints it out on the screen
###########################################################

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

    OUTPUT.write(identification + '\n' + DICTIONARY[identification] + '\n' + list_in_string + '\n')
    print(identification + '\n' + DICTIONARY[identification] + '\n' + list_in_string + '\n')
OUTPUT.close()
