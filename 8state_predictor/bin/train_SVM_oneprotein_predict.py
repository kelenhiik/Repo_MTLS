#####################################################
#import my functions from the all_parsing_codes file#
#####################################################
import all_parsing_codes
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
#tempfile = './11_proteins.txt'
#tempfile = '../data/train_test_sets/34_proteins.3line.txt'
unknown = './twoseq.txt'


##########################################################################################
#Split my dataset into 70% and 30%. 70% being the training set and 30% being the test set#
##########################################################################################
#input is the file used , windowsize

#X_train, Y_train, X_test, Y_test = all_parsing_codes.parse_with_train_test(tempfile, 11)

#print (X_train,'###', Y_train,'###')
#####################################
#fit the model with the training set#
#####################################

#clf = svm.SVC(kernel='linear', cache_size=3000)
#clf.fit(X_train, Y_train)


################
# Import model #
################

model = joblib.load('../src/small_models/RFC_predictor_smallmodel.pkl')

##########################
# Specify the windowsize #
##########################

sliding_window = 7

# This takes every sequence in a dicionary one at a time, predicts and then goes to the next one, also creates a file for it #

topology_dict={1:'G', 2:'I', 3:'H', 4:'E', 5:'B', 6:'T', 7:'S', 8:'C'}
output=open("../results/prediction_results/Prediction.txt",'w')
dictionary = all_parsing_codes.fasta_parsing_from_3lines(unknown)
for identification in dictionary:
    #print(identification)
    
    sw_of_unknown_topo_seq = all_parsing_codes.encode_protein((dictionary[identification]), sliding_window)
    sw_of_unknown_topo_seq = np.array(sw_of_unknown_topo_seq)
    prediction = model.predict(sw_of_unknown_topo_seq)
    prediction_states = prediction.tolist()
    list_of_ss = []

    for number in prediction_states:

        list_of_ss.extend(topology_dict[number])


    list_in_string = "".join(list_of_ss)

    output.write(identification + '\n' + dictionary[identification] + '\n' + list_in_string + '\n')
    print(identification + '\n' + dictionary[identification] + '\n' + list_in_string + '\n')
output.close()



