import all_parsing_codes
from sklearn import svm

X,Y=(all_parsing_codes.parse_with_all_codes('8_state_smallerset.3line.txt',11))
clf = svm.SVC()
clf.fit(X, Y) 
print(clf.score(X,Y))
