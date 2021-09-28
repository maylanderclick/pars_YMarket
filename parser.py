from bs4 import BeautifulSoup
import requests
import time


def parser(data):

    soup = BeautifulSoup(data, 'lxml')
    values = soup.findAll('div', attrs={'itemprop': 'review'})
    print(soup)

    for value in values:

        date_review = value.find('meta', attrs={'itemprop': 'datePublished'})
        print(date_review['content'])

        author = value.find('meta', attrs={'itemprop': 'author'})
        print(author['content'])

        review_rating = value.find('div', attrs={'itemprop': 'reviewRating'})
        print(review_rating.meta['content'])

        review = value.find('meta', attrs={'itemprop': 'description'})
        print(review['content'])

        print()


def url_next_page(data):
    soup = BeautifulSoup(data, 'lxml')
    value = soup.find('a', attrs={'aria-label': 'Следующая страница'})

    if value is None:
        return None
    else:
        return 'https://market.yandex.ru/' + value['href']


headers = {'Accept': 'text/html, application/xhtml+xml, application/xml; q = 0.9, image/avif, image/webp, image/apng, */*; q = 0.8, application/signed-exchange; v = b3; q = 0.9',
           'Accept-Language': 'ru-RU, ru;q = 0.9, en-US;q = 0.8, en;q = 0.7',
           'Connection': 'keep-alive',
           'Host': 'market.yandex.ru',
           'Sec-Fetch-Dest': 'document',
           'Sec-Fetch-Mode': 'navigate',
           'Sec-Fetch-Site': 'same-origin',
           'Sec-Fetch-User': '?1',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (X11 Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36', }


url = 'https://market.yandex.ru/product--smartfon-apple-iphone-12-128gb/722974019/reviews?track=tabs'

while True:
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    data_page = response.text
    parser(data_page)

    time.sleep(20)

    url = url_next_page(data_page)

    if url is None:
        break
