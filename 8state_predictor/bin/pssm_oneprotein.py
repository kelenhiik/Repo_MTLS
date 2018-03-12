"""Train with PSSM and predict on another two"""

#####################################################
#import my functions from the all_parsing_codes file#
#####################################################
import numpy as np
from sklearn import svm
import all_parsing_codes


TEMPFILE = './11_proteins.txt'
#tempfile = '../data/train_test_sets/34_proteins.3line.txt'
UNKNOWN = './twoseq.txt'
SLIDING_WINDOW = 11

##########################################################################################
#Split my dataset into 70% and 30%. 70% being the training set and 30% being the test set#
##########################################################################################

X_TRAIN, Y_TRAIN, X_TEST, Y_TEST = all_parsing_codes.protein_w_pssm_train(TEMPFILE, SLIDING_WINDOW)

#####################################
#fit the model with the training set#
#####################################

CLF = svm.SVC(kernel='linear', cache_size=3000)
CLF.fit(X_TRAIN, Y_TRAIN)

################################################################################
# This takes every sequence in a dicionary one at a time, predicts and then goes
# to the next one, also creates a file for it
################################################################################

TOPOLOGY_DICT = {1:'G', 2:'I', 3:'H', 4:'E', 5:'B', 6:'T', 7:'S', 8:'C'}

### output filename ###
OUTPUT = open("prediction_pssm.txt", 'w')
DICTIONARY = all_parsing_codes.fasta_parsing_from_3lines(UNKNOWN)
for identification in DICTIONARY:
    pssm_array = all_parsing_codes.pssm_format('../data/PSSM/' + identification + '.fasta.pssm')
    print(identification)

    sw_of_unknown_topo_pssm = all_parsing_codes.slide_pssm_windows(pssm_array, SLIDING_WINDOW)
    sw_of_unknown_topo_pssm = np.array(sw_of_unknown_topo_pssm)
    prediction = CLF.predict(sw_of_unknown_topo_pssm)
    prediction_states = prediction.tolist()
    list_of_ss = []

    for number in prediction_states:

        list_of_ss.extend(TOPOLOGY_DICT[number])


    list_in_string = "".join(list_of_ss)

    OUTPUT.write(identification + '\n' + DICTIONARY[identification] + '\n' + list_in_string + '\n')
OUTPUT.close()
