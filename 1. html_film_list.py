import requests, time
from bs4 import BeautifulSoup
import pandas as pd

url_list = []
for year in [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]:
    url_list.append('https://www.kinopoisk.ru/top/navigator/m_act%5Byear%5D/' + str(year) + '/m_act%5Brating%5D/1%3A/order/runtime/perpage/200/#results')
    url_list.append('https://www.kinopoisk.ru/top/navigator/m_act%5Byear%5D/' + str(year) + '/m_act%5Brating%5D/1%3A/order/runtime/page/2/#results')

movie_link = []
movie_name = []

for url in url_list:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    film_list = soup.find_all('div', {'class': 'item _NO_HIGHLIGHT_'})
    for film in film_list:
        movie_link.append(film.find('div', {'class': 'name'}).find('a').get('href'))
        movie_name.append(film.find('div', {'class': 'name'}).find('a').text)
    print(film_list.__len__())
    time.sleep(5)

movies = pd.DataFrame({'link': movie_link, 'name': movie_name})

writer = pd.ExcelWriter('movies.xlsx', engine='xlsxwriter')
movies.to_excel(writer, index=False, sheet_name='movies')
workbook = writer.book
worksheet = writer.sheets['movies']
header_fmt = workbook.add_format({'bold': True})
worksheet.set_row(0, None, header_fmt)
writer.save()