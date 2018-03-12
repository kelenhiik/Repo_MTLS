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

X_train, Y_train, X_test, Y_test = all_parsing_codes.protein_w_pssm_train(tempfile, 11)
#print (X_test)
#print (X_train.shape)

#####################################
#fit the model with the training set#
#####################################

clf = svm.SVC(kernel='linear', cache_size=3000)
clf.fit(X_train, Y_train)

#########################################################################
#use the testing set's feature to see if predicting works for the labels#
#########################################################################

#scoring=clf.score(X_test, Y_test)
#print (scoring)
prediction = clf.predict(X_test)
#############################################################################
#Retranslate the output to secondary structure elements as described by DSSP#
#############################################################################

topology_dict={1:'G', 2:'I', 3:'H', 4:'E', 5:'B', 6:'T', 7:'S', 8:'C'}

prediction_states=prediction.tolist()
list_of_ss=[]


for number in prediction_states:

    list_of_ss.extend(topology_dict[number])

##############################################################
#write the output into a txt.file, in case this is also necessary#
##############################################################
#list_in_string="".join(list_of_ss)

#output=open("prediction.txt",'w')
#output.write(list_in_string)
#output.close()

#when using these files, the output ss is in the length 14914. So this is giving the ss to all the proteins it is predicting it for....

print(list_of_ss)
