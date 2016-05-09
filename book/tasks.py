#  from __future__ import absolute_import
from multiprocessing import Pool
from author.models import Author
from .models import Tag, Book
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
    book_items = soup.select('li.s-result.item')
    links = [l.attrs.get('href') for l in soup.select('a.s-access-detail-page')]
    links = filter(lambda x: x.startswith('http://'), links)
    return links

def get_book_data(url, keyword):
    """
    Scrape individual book info by following its link
    """
    # tag = Tag.objects.get_or_create(name=keyword)

    response = requests.get(url, headers=HEADERS)
    soup = bs4.BeautifulSoup(response.text, 'lxml')

    tag, created = Tag.objects.get_or_create(keyword.lower())

    author_name = soup.select('span.author a[data-asin]')[0].text
    author_link = 'http://www.amazon.com/' + soup.select('a.contributorNameID')[0].attrs.get('href')
    bio, image = get_author_info(author_link)
    author = Author(name=author_name, bio=bio, image=image)
    author.save()

    title = soup.select('span#productTitle')[0].text
    desc = soup.select('#bookDescription_feature_div noscript')[0].text.strip()
    price = float(soup.select('span.a-color-price')[0].text.strip()[1:])
    rating_text = soup.select('a[href="#customerReviews"] span.a-icon-alt')[0].text
    rating = float(rating_text[:rating_text.find('out') - 1])
    image = soup.select('img#imgBlkFront')[0].attrs.get('src').strip()

    book = Book(title=title, description=desc, author=author, price=price,
                rating=rating, image=image)
    book.tags.add(tag)
    book.save()


    return (title, author_name, price, rating_text, rating, image)

def get_author_info(url):
    response = requests.get(url, headers=HEADERS)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    try:
        bio = soup.select('div#ap-bio span')[0].text.strip()
        image = soup.select('.ap-author-image')[0].attrs.get('src')
        return bio, image
    except IndexError:
        return None, None