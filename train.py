import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import cross_val_score
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.svm import LinearSVC
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

reviews = pd.read_excel('reviews_normal_2700.xlsx')

# print(reviews.target.value_counts(normalize=True))

# #Graphics
target_count = reviews.groupby(['target']).movie_link.count()
target_count_sum = target_count.sum()
target_count_percent = target_count/target_count_sum
target_count.sort_values(ascending=False, inplace=True)
print("All items " + str(target_count_sum) + ':')
print(target_count)

print("Percntage:")
print(target_count_percent)

# ax = target_count.plot(kind='bar')
# plt.show()

BagOfWordSubtitle = CountVectorizer()
BagOfWordText = CountVectorizer()

valuable_target = []
for target in reviews.target:
    if target == 'bad': valuable_target.append(0)
    if target == 'neutral': valuable_target.append(1)
    if target == 'good': valuable_target.append(2)

review_subtitle_v = BagOfWordSubtitle.fit_transform(reviews['normal_review_subtitle'].values.astype('U'))
review_text_v = BagOfWordText.fit_transform(reviews['normal_review_text'].values.astype('U'))

# reviews['review_subtitle_v'] = review_subtitle_v
# reviews['review_text_v'] = review_text_v
# reviews['valuable_target'] = valuable_target

# X_train, X_test, Y_train, Y_test = train_test_split(review_text_v,
#                                                     valuable_target, test_size=0.3)

print('Shape of review_text_v:' + str(review_text_v.shape))

clf = LinearSVC()
print('cross_val_score:' + str(cross_val_score(clf, review_text_v, valuable_target)))
