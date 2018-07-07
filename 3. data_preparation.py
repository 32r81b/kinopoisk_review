# -*- coding: utf-8 -*-
import pandas as pd
import re, pymorphy2

print('Start loading reviews_2700.xlsx')
reviews = pd.read_excel('reviews_2700.xlsx')
print('Loading finished')

morph = pymorphy2.MorphAnalyzer()

def normal_text(text):
    cleaned_string = re.sub(r'ё', r'е', str(text))
    cleaned_string = re.sub(r'Ё', r'Е', str(cleaned_string))
    cleaned_string = re.sub(r'[^А-я]', r' ', str(cleaned_string))
    words = re.split(r' ', cleaned_string)
    normal_string = []
    for word in words:
        if word != r'':
            p = morph.parse(word)[0]
            normal_string.append(p.normal_form)
    return ' '.join(normal_string)

normal_review_subtitle =[]
normal_review_text = []

i = 0
for review_subtitle in reviews.review_subtitle:
    normal_review_subtitle.append(normal_text(review_subtitle))
    i = i + 1
    if i % 1000 == 0:
        print('review_subtitle finished ' + str(i) + ' examples')

i = 0
for review_text in reviews.review_text:
    normal_review_text.append(normal_text(review_text))
    i = i + 1
    if i % 1000 == 0:
        print('review_text finished ' + str(i) + ' examples')

reviews['normal_review_subtitle'] = normal_review_subtitle
reviews['normal_review_text'] = normal_review_text
del reviews['review_text']
del reviews['review_subtitle']

name = 'reviews_normal_full.xlsx'

print('Saving to ' + name)
writer = pd.ExcelWriter(name, engine='xlsxwriter')
reviews.to_excel(writer, index=False, sheet_name='reviews')
workbook = writer.book
worksheet = writer.sheets['reviews']
header_fmt = workbook.add_format({'bold': True})
worksheet.set_row(0, None, header_fmt)
writer.save()