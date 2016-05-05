#  from __future__ import absolute_import
from multiprocessing import Pool
import requests
import bs4

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36'}

def get_books_links(keyword=''):
    """
    Retrieve book links from the search page
    """
    AMAZON = 'http://www.amazon.com/s/?field-keywords=%s'
    response = requests.get(AMAZON % keyword, headers=HEADERS)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    links = [l.attrs.get('href') for l in soup.select('a.s-access-detail-page')]
    return links

def get_book_data(url):
    """
    Scrape individual book info by following its link
    """
    response = requests.get(url, headers=HEADERS)
    soup = bs4.BeautifulSoup(response.txt, 'lxml')
    title = soup.select('span#productTitle')[0].text
    author_name = soup.select('span.author a[data-asin]')[0].text
    price = float(soup.select('span.a-color-price')[0].text[1:])
    rating_text = soup.select('a[href="#customerReviews] span.a-icon-alt')[0].text
    rating = rating_text[:rating_text.find('out') - 1]
    url =




print scrape_page(keyword='javascript')