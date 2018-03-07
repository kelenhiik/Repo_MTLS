#####################################################
#import my functions from the all_parsing_codes file#
#####################################################
import all_parsing_codes
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
tempfile = './34_proteins.3line.txt'
#tempfile = '../data/train_test_sets/34_proteins.3line.txt'
unknown = './oneseq.txt'


##########################################################################################
#Split my dataset into 70% and 30%. 70% being the training set and 30% being the test set#
##########################################################################################
#input is the file used , windowsize

X_train, Y_train, X_test, Y_test = all_parsing_codes.parse_with_train_test(tempfile, 11)

#print (X_train,'###', Y_train,'###')
#####################################
#fit the model with the training set#
#####################################

clf = svm.SVC(kernel='linear', cache_size=3000)
clf.fit(X_train, Y_train)

#########################################################################
#use a hardcoded sequence for predicting#
#########################################################################
#Notice, not using the test set anywhere at the moment, since I want to see how it works for one sequence.#

Test, id_of_test, seq_of_test = all_parsing_codes.parse_unknown_file(unknown, 11)

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


output=open("prediction2.txt",'w')
output.write(id_of_test + '\n' + seq_of_test + '\n' + list_in_string)
output.close()




