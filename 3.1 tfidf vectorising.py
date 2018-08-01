import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import cross_val_score
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.svm import LinearSVC
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import SGDClassifier

reviews = pd.read_excel('reviews_normal_full.xlsx')
# stopwords = pd.read_excel('stopwords.xlsx')
# stopword_list = stopwords['word'][stopwords.stop_flag == 1].values.tolist()

Vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=2)

review_text_v = Vectorizer.fit_transform(reviews['normal_review_text'].values.astype('U'))

import numpy as np
from scipy.sparse import csr_matrix

def save_sparse_csr(filename, array):
    # note that .npz extension is added automatically
    np.savez(filename, data=array.data, indices=array.indices,
             indptr=array.indptr, shape=array.shape)
def load_sparse_csr(filename):
    # here we need to add .npz extension manually
    loader = np.load(filename + '.npz')
    return csr_matrix((loader['data'], loader['indices'], loader['indptr']),
                      shape=loader['shape'])

save_sparse_csr('review_text_v_ngram12_mindf2', review_text_v)