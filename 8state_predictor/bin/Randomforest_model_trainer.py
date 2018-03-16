""" This script trains a model using a random forest classifier """
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier as RFC
import pickle
import all_parsing_codes

#######################################
# Enter the path to your training set #
#######################################

tempfile = '../data/train_test_sets/randomized109_proteins.3line.txt'
UNKNOWN  = '../data/testing_sets/dataset_of_50.txt'
#############################################
# Enter parameter values you wish to change #
#############################################
win_len = 11
n_estimators1 = 300
min_samples_split1 = 5

###########################################################################
# Retrieve your training information, this is going to parse a whole file #
###########################################################################
X_train, Y_train, X_test, Y_test = all_parsing_codes.parse_with_train_test(tempfile, win_len)
z_test, o_test = all_parsing_codes.parse_with_all_codes(UNKNOWN, win_len)
#######################################################
# Create a model with the before-mentioned parameters #
#######################################################

RFC_predictor_model = RFC(n_estimators = n_estimators1, min_samples_split = min_samples_split1, n_jobs = -1)


RFC_predictor_model.fit(X_train, Y_train)
score = RFC_predictor_model.score(z_test, o_test)

##################
# Save the model #
##################
"""
location = '../src/small_models/RFC_PSFM_predictor_109.pkl'
out_location = open(location, 'wb')
pickle.dump(RFC_predictor_model, out_location)
out_location.close()
"""
print("RFC_predictor_model score for external proteins: " + str(score))

