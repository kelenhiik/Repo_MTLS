""" This predicts topology from an input file using a trained model """
#####################################################
#import my functions from the all_parsing_codes file#
#####################################################
import all_parsing_codes
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib

unknown = './twoseq.txt'
#unknown_fasta = './2protein.fasta'

################
# Import model #
################

model = joblib.load('../src/small_models/RFC_predictor_smallmodel.pkl')

######################################################################
# Specify the windowsize, must be 7 since I trained my model with it #
######################################################################

sliding_window = 7

topology_dict={1:'G', 2:'I', 3:'H', 4:'E', 5:'B', 6:'T', 7:'S', 8:'C'}

#### Specify the path and filename for results, default is the following:

output=open("../results/prediction_results/Prediction.txt",'w')

############################################################################################
# If you want to use a file that has three lines: ID, seq, topology, but want to leave the #
# topology out and receive the predicted topology, use this and comment the other one out #
############################################################################################

dictionary = all_parsing_codes.fasta_parsing_from_3lines(unknown)

#################################################################################################
# If you want to use a file that has two lines: ID, seq. OR any fasta file with the same format,#
# use this and comment the above one out
#################################################################################################

#dictionary = all_parsing_codes.fasta_parser_onlyseq(unknown_fasta)

##################################################################################################
# This takes every sequence in a dicionary one at a time, predicts and then goes to the next one,#
#also creates a file for it #
##################################################################################################

for identification in dictionary:
    
    
    sw_of_unknown_topo_seq = all_parsing_codes.encode_protein((dictionary[identification]), sliding_window)
    sw_of_unknown_topo_seq = np.array(sw_of_unknown_topo_seq)
    prediction=model.predict(sw_of_unknown_topo_seq)
    prediction_states=prediction.tolist()
    list_of_ss=[]

    for number in prediction_states:

        list_of_ss.extend(topology_dict[number])


    list_in_string="".join(list_of_ss)

# it also prints it on the terminal screen

    output.write(identification + '\n' + dictionary[identification] + '\n' + list_in_string + '\n')
    print(identification + '\n' + dictionary[identification] + '\n' + list_in_string + '\n')
output.close()



