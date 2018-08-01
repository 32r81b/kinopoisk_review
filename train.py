import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import cross_val_score
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.svm import LinearSVC, SVC
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import SGDClassifier

reviews = pd.read_excel('reviews_normal_full.xlsx')
Vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=2)

valuable_target = []
for target in reviews.target:
    if target == 'bad': valuable_target.append(0)
    if target == 'neutral': valuable_target.append(1)
    if target == 'good': valuable_target.append(2)

del reviews

import numpy as np
from scipy.sparse import csr_matrix

def load_sparse_csr(filename):
    # here we need to add .npz extension manually
    loader = np.load(filename + '.npz')
    return csr_matrix((loader['data'], loader['indices'], loader['indptr']),
                      shape=loader['shape'])

review_text_v = load_sparse_csr('review_text_v_ngram12_mindf2')

# TfidfVectorizer(ngram_range=(1, 2))          Shape of review_text_v:(80284, 2380424)
# --- LinerSVC()
#                                              - 0.821708278902394
# min_df=2                                     - 0.82245562350097
# min_df=2, tol=0.2                            - 0.8225801813214636
# min_df=2, tol=0.2 храню матрицу в файле      - 0.8226050871451782

# --- SGDClassifier()
# alpha=0.001                                  - 0.7497010626278673
# alpha=0.0001                                 - 0.7580341291292931
# alpha=0.00001                                - 0.7580714556688298

print('Shape of review_text_v:' + str(review_text_v.shape))

param_grid = [{'tol': [0.00001, 0.0001, 0.001, 0.01, 0.1, 1]}]

clf = SVC(kernel='linear')

accuracy = cross_val_score(clf, review_text_v, valuable_target, cv=5, scoring='accuracy')
print('cross_val_score mean:' + str(np.mean(accuracy)))

# print('cross_val_score:' + str(accuracy))