from sklearn.metrics import confusion_matrix
from sklearn import svm
import itertools
from sklearn.ensemble import RandomForestClassifier as RFC
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

import all_parsing_codes


TEMPFILE = '../data/train_test_sets/randomized109_proteins.3line.txt'
TEMPFILE2 = '../data/testing_sets/dataset_of_50.txt'
win_len = 7
class_names = ['G', 'I', 'H', 'E', 'B', 'T', 'S', 'C']
X_train, y_train, e, o = all_parsing_codes.parse_with_train_test(TEMPFILE, win_len)
X_test, y_test = all_parsing_codes.parse_with_all_codes(TEMPFILE2, win_len)
#X_train, y_train, X_test, y_test = all_parsing_codes.protein_w_pssm_train(TEMPFILE,win_len)

classifier_model = RFC(n_estimators = 350, min_samples_split = 2, n_jobs = -1)
y_pred = classifier_model.fit(X_train, y_train).predict(X_test)

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Greens):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

    # Compute confusion matrix
cnf_matrix = confusion_matrix(y_test, y_pred)
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Non-normalized confusion matrix for PSFM Random forests on external dataset')
plt.savefig('./extprot_non_norm.png')
# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
                      title='Normalized confusion matrix for PSFM Random forests on external dataset')
plt.savefig('./extprot_norm.png')
plt.show()
