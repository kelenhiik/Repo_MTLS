#####################################################
#import my functions from the all_parsing_codes file#
#####################################################
import all_parsing_codes
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score

tempfile = '../data/train_test_sets/34_proteins.3line.txt'



##########################################################################################
#Split my dataset into 70% and 30%. 70% being the training set and 30% being the test set#
##########################################################################################
#input is the file used , windowsize
X_train, Y_train, X_test, Y_test = all_parsing_codes.parse_with_train_test(tempfile, 11)

#####################################
#fit the model with the training set#
#####################################

clf = svm.SVC(kernel='linear', cache_size=3000)
clf.fit(X_train, Y_train)

#########################################################################
#use a hardcoded sequence for predicting#
#########################################################################
#Notice, not using the test set anywhere at the moment, since I want to see how it works for one sequence.#


hardcodedseq='KVFERaELARTLKRLGMDGYRGISLANWMbLAKWESQYNTRATNYNAGDRSTDYGIFQINSRYWcNDGKTPGAVNAdHLScSALLQDNIADAVAdAKRVVRDPQGIRAWVAWRNRbQNRDVRQYVQGaGV'
hardcodedseq_allupper=hardcodedseq.upper()
Test=[]

#calling the protein encoding function from the other file#

sliding_window_of_unknown_seq = all_parsing_codes.encode_protein(hardcodedseq_allupper,11)
Test.extend(sliding_window_of_unknown_seq)



Test = np.array(Test)



prediction=clf.predict(Test)

#############################################################################
#Retranslate the output to secondary structure elements as described by DSSP#
#############################################################################

topology_dict={1:'G', 2:'I', 3:'H', 4:'E', 5:'B', 6:'T', 7:'S', 8:'C'}

prediction_states=prediction.tolist()
list_of_ss=[]


for number in prediction_states:

    list_of_ss.extend(topology_dict[number])


list_in_string="".join(list_of_ss)

# This is what I get with this hardcoded sequences
#CCCHHHHHHHHHHHHCCTSCEHHHHHHHHHHHHHHHHHHHHHHHHHCSCCESCTHHEHTHIHEEECSCCCCSCHHHHHHHHHHHHHHHHHHHHHHHHEEEECTTHHEHEEHHHCHCCTHHHHHEEHTCSC

# This is what it should be for >d1b7o
#CBCCHHHHHHHHHHTTCTTBTTBCHHHHHHHHHHHHSSBTTCEEEETTTTEEEETTTTEETTTTCBCSCSTTCCCTTCCBGGGGGSSSCHHHHHHHHHHTTSTTGGGGSHHHHHHTTTSCCGGGTTTSCC
# This protein is not in the training set.


print(list_in_string)
