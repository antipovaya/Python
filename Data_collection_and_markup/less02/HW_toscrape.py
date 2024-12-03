# Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию о всех книгах на сайте во всех
# категориях: название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.
#
# Затем сохранить эту информацию в JSON-файле.

import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
from fake_useragent import UserAgent  # pip install fake_useragent
from pprint import pprint

ua = UserAgent()

url = "https://books.toscrape.com"

# headers = {"User-Agent": ua.random}
headers = {"User-Agent": ua.chrome}
param = "/page-1.html"
session = requests.session()  # аналогия с открытой вкладкой

response = session.get(url + "/catalogue/" + param, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all('li', {'class': 'col-xs-6'})
all_books = []

for book in books:
    book_info = {}

    name_info = book.find('h3')
    book_info['name'] = name_info.find('a').getText()
    book_info['url'] = url + "/catalogue/" + name_info.find('a').get('href')

    price_info = float(book.find('div', {"class": 'product_price'}).find('p', {"class": 'price_color'}).getText()[2:])
    book_info['price'] = price_info

    stock_info = book.find('div', {"class": 'product_price'}).find('p', {"class": 'instock availability'}).getText()
    if 'In stock' in stock_info:
        book_info['stock'] = 'yes'
    else:
        book_info['stock'] = 'no'

    all_books.append(book_info)
pprint(all_books)


