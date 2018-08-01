# -*- coding: utf-8 -*-
import pandas as pd
import re, xlsxwriter

print('Start loading reviews_normal_full.xlsx')
reviews = pd.read_excel('reviews_normal_full.xlsx')
print('Loading finished')


i = 0
review_text_dict = {}
for review_text in reviews.normal_review_text:
    # print('review_text: ' + str(review_text))
    review_text = re.sub(r'[^А-я0-9]', r' ', str(review_text))
    words = re.split(r' ', review_text)
    for word in words:
        if word in review_text_dict:
            review_text_dict[word] = review_text_dict[word] + 1
        else:
            review_text_dict[word] = 1

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for key in review_text_dict.keys():
    worksheet.write(row, col, key)
    worksheet.write(row, col + 1, review_text_dict[key])
    row += 1

workbook.close()