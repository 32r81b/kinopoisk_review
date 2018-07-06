import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_excel('reviews_100.xlsx')

#Graphics
target_count = reviews.groupby(['target']).movie_link.count()
target_count_sum = target_count.sum()
target_count_percent = target_count/target_count_sum
target_count.sort_values(ascending=False, inplace=True)

# ax = target_count.plot(kind='bar')
# plt.show()

