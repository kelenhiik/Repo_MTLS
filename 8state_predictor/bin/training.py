import all_parsing_codes
from sklearn import svm


#X,Y=(all_parsing_codes.parse_with_all_codes('100_proteins.3line.txt',11))
#unknown=(all_parsing_codes.parse_unknown_file('250_270_set.3line.txt', 11))
#clf = svm.SVC(kernel='linear') #model
#clf.fit(X, Y) 
#score=clf.score(X,Y)
#print(score)
topology_dict={1:'G', 2:'I', 3:'H', 4:'E', 5:'B', 6:'T', 7:'S', 8:'C'}
##########################################################################################
#Split my dataset into 70% and 30%. 70% being the training set and 30% being the test set#
##########################################################################################
X_train, Y_train, X_test, Y_test = all_parsing_codes.parse_with_train_test('34_proteins.3line.txt', 11)
#'../data/train_test_sets/34_proteins.3line.txt' - does not work, [Errno 20] not a directory... but it is...
#fit the model with the training set#
clf = svm.SVC(kernel='linear', cache_size=3000)
clf.fit(X_train, Y_train) 
################################################
#use the testing set to see if predicting works#
################################################
prediction=clf.predict(X_test)
prediction_states=prediction.tolist()
list_of_ss=[]
for number in prediction_states:

    list_of_ss.extend(topology_dict[number])


print(list_of_ss)


#for kernel in ('linear', 'rbf', 'polinomial'):
#   for c_par in (...):
#       clf = svm.SVC(kernel=kernel, cache_size=3000)
   
#       print(kernel, c_par, score)
