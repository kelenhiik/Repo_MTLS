""" This script trains a model using a random forest classifier """
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier as RFC
import pickle
import all_parsing_codes

#######################################
# Enter the path to your training set #
#######################################

tempfile = '../data/training_sets/randomized109_proteins.3line.txt'

#############################################
# Enter parameter values you wish to change #
#############################################
win_len = 11
n_estimators1 = 350
min_samples_split1 = 3

###########################################################################
# Retrieve your training information, this is going to parse a whole file #
###########################################################################
X_train, Y_train, X_test, Y_test = all_parsing_codes.parse_with_train_test(tempfile, win_len)

#######################################################
# Create a model with the before-mentioned parameters #
#######################################################

RFC_predictor_model = RFC(n_estimators = n_estimators1, min_samples_split = min_samples_split1, n_jobs = -1, class_weight = 'balanced')

# score = cross_val_score(RFC_predictor_model, X_train, Y_train, cv=5, verbose=True, n_jobs=-1)
# score=np.average(score)
# print(score)
# [Parallel(n_jobs=-1)]: Done   5 out of   5 | elapsed:  3.6min finished score: 0.542601619795

RFC_predictor_model.fit(X_train, Y_train)
score = RFC_predictor_model.score(X_test, Y_test)
print('Balanced window 11, nestimator 350, split 3, single sequence', str(score))
