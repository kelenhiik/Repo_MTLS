import all_parsing_codes
from sklearn import svm

#X,Y=(all_parsing_codes.parse_with_all_codes('100_proteins.3line.txt',11))
unknown=(all_parsing_codes.parse_unknown_file('250_270_set.3line.txt', 11))
#clf = svm.SVC(kernel='linear') #model
#clf.fit(X, Y) 
#score=clf.score(X,Y)
#print(score)


X_train, Y_train, X_test, Y_test = all_parsing_codes.parse_with_train_test('100_proteins.3line.txt', 11)

clf = svm.SVC(kernel='linear', cache_size=3000)
clf.fit(X_train, Y_train) 

prediction=clf.predict(X_test)


print('linear',  prediction )


#for kernel in ('linear', 'rbf', 'polinomial'):
#   for c_par in (...):
#       clf = svm.SVC(kernel=kernel, cache_size=3000)
   
#       print(kernel, c_par, score)
