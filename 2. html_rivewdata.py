import requests, time
from bs4 import BeautifulSoup
import pandas as pd

movies = pd.read_excel('movies.xlsx')

target = []
movie_link = []
author_id = []
author_name = []
review_subtitle = []
review_text = []

for i, movie in enumerate(movies.itertuples(), 1):
    movie_url = 'https://www.kinopoisk.ru' + movie.link + 'ord/rating/perpage/75/#list'
    print(str(i) + " " + movie.name + ": " + movie_url)
    r = requests.get(movie_url)
    soup = BeautifulSoup(r.text, "html.parser")
    review_list = soup.find_all('div', {'class': 'response good', 'class': 'response bad', 'class': 'response'})

    for review in review_list:
        target1 = review.get('class')
        if target1.__len__() == 2:
            target.append(target1[1])
        else:
            target.append("neutral")
        movie_link.append(movie.link)
        review_details = review.find('div', {'itemprop': 'author'}).find('div')
        author_name.append(review_details.find('p', {'class': 'profile_name'}).text)

        if review_details.find('p', {'class': 'profile_name'}).find('a'):
            author_id.append(review_details.find('p', {'class': 'profile_name'}).find('a').get('href'))
        else:
            author_id.append("0")

        review_subtitle.append(review.find('p', {'class': 'sub_title'}).text)
        review_text.append(review.find('span', {'itemprop': 'reviewBody'}).text)
        print("-" + str(review_details.find('p', {'class': 'profile_name'}).text))

    writer = pd.ExcelWriter('reviews.xlsx', engine='xlsxwriter')
    reviewDF = pd.DataFrame({'movie_link': movie_link, 'target': target, 'author_id': author_id,
                             'author_name': author_name, 'review_subtitle': review_subtitle, 'review_text': review_text})

    reviewDF.to_excel(writer, index=False, sheet_name='reviews')
    workbook = writer.book
    worksheet = writer.sheets['reviews']
    header_fmt = workbook.add_format({'bold': True})
    worksheet.set_row(0, None, header_fmt)
    writer.save()

    time.sleep(5)



