import all_parsing_codes
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier as RFC
tempfile = '../data/train_test_sets/34_proteins.3line.txt'





for n_estimators1 in (100,150,200,250,300,):
    for min_samples_split1 in range(2,9):
        for win_len in range(9,36,2):
            X_train, Y_train = all_parsing_codes.parse_with_all_codes('34_proteins.3line.txt', win_len)
            model= RFC(n_estimators=n_estimators1, min_samples_split = min_samples_split1, n_jobs=-1, class_weight='balanced')
            score = cross_val_score(model, X_train, Y_train, cv=3, verbose=True, n_jobs=-1)
            score=np.average(score)
            print( n_estimators1, min_samples_split1, win_len, score)
