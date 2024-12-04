import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
from fake_useragent import UserAgent  # pip install fake_useragent
from pprint import pprint
ua = UserAgent()


url = "https://gb.ru"

# headers = {"User-Agent": ua.random}
headers = {"User-Agent": ua.chrome}
params = {'page': 1}
session = requests.session()  # аналогия с открытой вкладкой

# response = session.get(url + "/posts", headers=headers, params=params)
# soup = BeautifulSoup(response.text, "html.parser")
# posts = soup.find_all('div', {'class': 'post-item event'})


all_posts = []

while True:
    response = session.get(url + "/posts", headers=headers, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    posts = soup.find_all('div', {'class': 'post-item event'})
    if not posts:
        break
    for post in posts:
        post_info = {}
        name_info = post.find('a', {"class": 'post-item__title h3 search_text'})
        post_info['name'] = name_info.getText()
        post_info['url'] = url + name_info.get('href')

        add_info = post.find('div', {'class': 'text-muted'}).findChildren('span')
        post_info['views'] = int(add_info[0].getText())
        post_info['comments'] = int(add_info[1].getText())
        all_posts.append(post_info)
    print(f'Обработана {params["page"]} страница')
    params['page'] += 1
pprint(all_posts)

