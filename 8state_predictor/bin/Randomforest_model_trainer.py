""" This script trains a model using a random forest classifier """
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier as RFC
import pickle
import gzip
import all_parsing_codes

#######################################
# Enter the path to your training set #
#######################################

tempfile = '../data/train_test_sets/randomized109_proteins.3line.txt'

#############################################
# Enter parameter values you wish to change #
#############################################
win_len = 7
n_estimators1 = 350
min_samples_split1 = 2
#PSFM
###########################################################################
# Retrieve your training information, this is going to parse a whole file #
###########################################################################
X_train, Y_train = all_parsing_codes.pssm_svm(tempfile, win_len)

#######################################################
# Create a model with the before-mentioned parameters #
#######################################################

RFC_predictor_model = RFC(n_estimators = n_estimators1, min_samples_split = min_samples_split1, n_jobs = -1)





RFC_predictor_model.fit(X_train, Y_train)

##################
# Save the model #
##################
location = '../src/small_models/8SS_RFC_PSFM_predictor_model.pklz'
out_location = gzip.open(location, 'wb')
pickle.dump(RFC_predictor_model, out_location, protocol=-1)
out_location.close()
