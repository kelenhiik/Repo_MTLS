import all_parsing_codes
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
#from sklearn.model_selection import KFold
#from sklearn.model_selection import GridSearchCV
#import pandas as pd
import matplotlib.pyplot as plt
tempfile = '../data/train_test_sets/34_proteins.3line.txt'
# X,Y=(all_parsing_codes.parse_with_all_codes('100_proteins.3line.txt',11))
# unknown=(all_parsing_codes.parse_unknown_file('250_270_set.3line.txt', 11))
# clf = svm.SVC(kernel='linear') #model
# clf.fit(X, Y) 
# score=clf.score(X,Y)
# print(score)
topology_dict={1:'G', 2:'I', 3:'H', 4:'E', 5:'B', 6:'T', 7:'S', 8:'C'}

##########################################################################################
# Split my dataset into 70% and 30%. 70% being the training set and 30% being the test set#
##########################################################################################

# X_train, Y_train, X_test, Y_test = all_parsing_codes.parse_with_train_test('34_proteins.3line.txt', 11)
# '../data/train_test_sets/34_proteins.3line.txt' - does not work, [Errno 20] not a directory... but it is...

# fit the model with the training set#

# clf = svm.SVC(kernel='linear', cache_size=3000)
# clf.fit(X_train, Y_train) 

################################################
# use the testing set to see if predicting works#
################################################

# prediction=clf.predict(X_test)
# prediction_states=prediction.tolist()
# list_of_ss=[]

# for number in prediction_states:

    # list_of_ss.extend(topology_dict[number])


# print(list_of_ss,a)


# for kernel in ('linear', 'rbf', 'polinomial'):
#   for c_par in (...):
#       clf = svm.SVC(kernel=kernel, cache_size=3000)
   
#       print(kernel, c_par, score)


'''for c_score in (0.1, 0.5, 1, 1.5, 5, 10):
    for decision_function_shape1 in ('ovo', 'ovr'):
        for kernel1 in ('linear', 'poly', 'rbf', 'sigmoid'):
            for win_len in range(9,20,2):
                X_train, Y_train = all_parsing_codes.parse_with_all_codes('34_proteins.3line.txt', win_len)
                model=svm.SVC(kernel=kernel1, gamma=1/X_train.shape[1], C= c_score, decision_function_shape=decision_function_shape1 ,cache_size=3000)
                score = cross_val_score(model, X_train, Y_train, cv=3, verbose=True, n_jobs=-1)
                score=np.average(score)
                print(c_score, decision_function_shape1, kernel1, win_len, score)'''
plapla = open('../results/windows_svm_results.txt', 'w')
win_list = []
score_ave_list = []
score_std_list = []
for win_len in range(9,26,2):
                X_train, Y_train = all_parsing_codes.parse_with_all_codes('34_proteins.3line.txt', win_len)
                model=svm.SVC(cache_size=3000)
                score = cross_val_score(model, X_train, Y_train, cv=5, verbose=True, n_jobs=-1)
                ave=np.average(score)
                std=np.std(score)
                win_list.append(win_len)
                score_ave_list.append(ave)
                score_std_list.append(std)
                plapla.write(str(win_len) + ',' + str(ave) + ',' + str(std))
                print(win_len, ave)
                
plapla.close()

plt.figure()

plt.title("score of window length")
plt.xlabel("Window Size")
plt.ylabel("score")

plt.plot(win_list, score_ave_list, 'o-', label='mean')
plt.show()
  

'''
for win_len in range(7,36,2):
            X_train, Y_train = all_parsing_codes.parse_with_all_codes('34_proteins.3line.txt', win_len)
            svc = svm.SVC(cache_size=3000)
            C_range = [1, 5, 10, 50, 100]
            gamma_range = [0.001, 0.01]
            parameters = {'C': C_range, 'gamma': gamma_range}
            clf = GridSearchCV(svc, parameters, n_jobs=-1, cv=3, verbose=2, error_score=np.NaN, return_train_score=False)
            clf.fit(X_train, Y_train)
            df = pd.DataFrame(clf.cv_results_)
            filename = '../results/grid_rbf_' + str(win_len) + '.csv'
            df.to_csv(filename, sep='\t', encoding='utf-8')

          
            
for decision_function_shape1 in ('ovo', 'ovr'):
    for kernel1 in ('linear', 'rbf',):
        for win_len in range(19,36,2):
            X_train, Y_train = all_parsing_codes.parse_with_all_codes('34_proteins.3line.txt', win_len)
            model=svm.SVC(kernel=kernel1, gamma=1/X_train.shape[1], C= 10, decision_function_shape=decision_function_shape1 ,cache_size=3000)
            score = cross_val_score(model, X_train, Y_train, cv=3, verbose=True, n_jobs=-1)
            score=np.average(score)
            print(decision_function_shape1, kernel1, win_len, score)
'''

