import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.metrics import classification_report
from sklearn import svm
import all_parsing_codes

TEMPFILE = '../data/train_test_sets/randomized109_proteins.3line.txt'
#OUTPUT = open("../results/testing_results/linearSVM_metrics.txt", 'w')
#OUTPUT2 = open("../results/testing_results/linearSVM_crossvalidation.txt", 'w')

"""
for c_score in (0.1, 1, 10, 100):
    for win_len in range(5,22,2):
        X_TRAIN, Y_TRAIN, X_TEST, Y_TEST = all_parsing_codes.parse_with_train_test(TEMPFILE,
                                                                                   win_len)
        MODEL = svm.LinearSVC(C=c_score)
        MODEL.fit(X_TRAIN, Y_TRAIN,)
        PREDICTION = MODEL.predict(X_TEST)
        REPORT = classification_report(Y_TEST, PREDICTION, labels=[1, 2, 3, 4, 5, 6, 7, 8],
                                       target_names=['G', 'I', 'H', 'E', 'B', 'T', 'S', 'C'])
        CONFUSION = confusion_matrix(Y_TEST, PREDICTION, labels=[1, 2, 3, 4, 5, 6, 7, 8])
        MATTHEW = matthews_corrcoef(Y_TEST, PREDICTION)
        print (type(CONFUSION))

        OUTPUT.write('Window length: ' + '\n' + str(win_len) + '\n' +
                     'C-score: ' + '\n' + str(c_score) + '\n' +
                     'Classification report: ' + '\n' + str(REPORT) + '\n' +
                     'Confusion matrix: ' + '\n' + str(CONFUSION) + '\n' +
                     'Matthews correlation: ' + '\n' + str(MATTHEW) + '\n')
        print('Window length: ' + str(win_len),
              'C-score: ' + str(c_score),
              'Classification report: ' + str(REPORT),
              'Confusion matrix: ' + str(CONFUSION),
              'Matthews correlation: ' + str(MATTHEW))


OUTPUT.close()
"""



X_TRAIN, Y_TRAIN, X_TEST, Y_TEST = all_parsing_codes.parse_with_train_test(TEMPFILE,
                                                                                   11)
MODEL = RFC(n_estimators = 350, min_samples_split = 3, n_jobs = -1, class_weight='balanced')

SCORE = cross_val_score(MODEL, X_TRAIN, Y_TRAIN, cv=3, verbose=True, n_jobs=-1)
SCORE_AVERAGE = np.average(SCORE)
SCORE_DEVIATION = np.std(SCORE)

print( 'Balanced single seq AVERAGE CV: ' + str(SCORE_AVERAGE) + 'DEVIATION' + str(SCORE_DEVIATION))
