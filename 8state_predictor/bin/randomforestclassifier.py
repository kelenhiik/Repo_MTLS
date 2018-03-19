import all_parsing_codes
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier as RFC
import numpy as np
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import all_parsing_codes

tempfile = '../data/train_test_sets/randomized109_proteins.3line.txt'
TEMPFILE2 = '../data/testing_sets/dataset_of_50.txt'
OUTPUT = open("../results/testing_results/RFC_metrics_again.txt", 'w')


X_TRAIN, Y_TRAIN, X_TEST, Y_TEST = all_parsing_codes.parse_with_train_test(tempfile, 11)

MODEL = RFC(n_estimators=350, min_samples_split = 3, 
            n_jobs=-1)
MODEL.fit(X_TRAIN, Y_TRAIN,)
PREDICTION = MODEL.predict(X_TEST)
REPORT = classification_report(Y_TEST, PREDICTION, labels=[1, 2, 3, 4, 5, 6, 7, 8], 
                               target_names=['G', 'I', 'H', 'E', 'B', 'T', 'S', 'C'])
CONFUSION = confusion_matrix(Y_TEST, PREDICTION, labels=[1, 2, 3, 4, 5, 6, 7, 8])
MATTHEW = matthews_corrcoef(Y_TEST, PREDICTION)
#print (type(CONFUSION))
            
OUTPUT.write('Window length: ' + '\n' + str(11) + '\n' +
             'N-estimators: ' + '\n' + str(350) + '\n' +
             'Min_samples_split: ' + '\n' + str(3) + '\n' +
             'Classification report: ' + '\n' + str(REPORT) + '\n' +
             'Confusion matrix: ' + '\n' + str(CONFUSION) + '\n' +
             'Matthews correlation: ' + '\n' + str(MATTHEW) + '\n')
print('Window length: ' + str(11),
      'N-estimators: ' + str(350),
      'Min_samples_split: ' + str(3),
      'Classification report: ' + str(REPORT),
      'Confusion matrix: ' + str(CONFUSION),
      'Matthews correlation: ' +  str(MATTHEW))
      
                 

OUTPUT.close()
"""

TOPOLOGY_DICT = {'G':1, 'I':2, 'H':3, 'E':4, 'B':5, 'T':6, 'S':7, 'C':8}

for n_estimators1 in (10, 100, 200, 300, 350):
    for win_len in range(5,22,2):
        for min_samples_split1 in range(2,9):
            X_TRAIN, Y_TRAIN, X_TEST, Y_TEST = all_parsing_codes.parse_with_train_test(TEMPFILE, 
                                                                                       win_len)
            MODEL = RFC(n_estimators=n_estimators1, min_samples_split = min_samples_split1, 
                        n_jobs=-1)
            SCORE = cross_val_score(MODEL, X_TRAIN, Y_TRAIN, cv=3, verbose=True, n_jobs=-1)
            SCORE_AVERAGE = np.average(SCORE)
            SCORE_DEVIATION = np.std(SCORE)
            OUTPUT2.write('N-estimators: '  + str(n_estimators1) + '\n' + " window size: "  + str(win_len) + '\n' + "Min-samples-split: " + str(min_samples_split1) + '\n' + " cross-validation score: " + str(SCORE_AVERAGE) + '\n' + " standard deviation: " + str(SCORE_DEVIATION) + '\n')
            print('N-estimators: ' + str(n_estimators1), " window size: " + 
                          str(win_len), "Min-samples-split: " + str(min_samples_split1), 
                          " cross-validation score: " + str(SCORE_AVERAGE), " standard deviation: " + str(SCORE_DEVIATION))
            
        
OUTPUT2.close()"""
