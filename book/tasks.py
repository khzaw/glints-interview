from __future__ import absolute_import
from itertools import cycle
from author.models import Author
from .models import Tag, Book
import requests
import bs4
import time

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36'}

def get_books_links(keyword=''):
    """
    Retrieve book links from the search page
    """
    AMAZON = 'http://www.amazon.com/s/?field-keywords=%s'
    response = requests.get(AMAZON % keyword, headers=HEADERS)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    #  book_items = soup.select('li.s-result.item')
    links = [l.attrs.get('href') for l in soup.select('a.s-access-detail-page')]
    links = filter(lambda x: x.startswith('http://'), links)
    return links

TEXT = 1
ATTR = 2
def retrieve(soup, selector, str_type=TEXT, attr=''):
    try:
        s = soup.select(selector)[0]
        if str_type == TEXT:        # either the text inside <tag> or attr
            return s.text.strip()
        return s.attrs.get(attr).strip()
    except IndexError:
        return None



def get_book_data(url, keyword):
    """
    Scrape individual book info by following its link
    """

    response = requests.get(url, headers=HEADERS)
    soup = bs4.BeautifulSoup(response.text, 'lxml')

    tag, created = Tag.objects.get_or_create(name=keyword.lower())

    title = retrieve(soup, 'span#productTitle') or \
            retrieve(soup,  '#booksTitle span.a-size-extra-large')
    if not title:
        return

    print 'Scraping %s' % title

    desc = retrieve(soup, '#bookDescription_feature_div noscript')

    price = float(retrieve(soup, 'span.a-color-price')[1:].split('-')[0].strip())
    rating_text = retrieve(soup, 'a[href="#customerReviews"] span.a-icon-alt')
    if rating_text:
        rating = float(rating_text[:rating_text.find('out') - 1])
    else:
        rating = 0.0
    book_image = retrieve(soup, 'img#imgBlkFront', str_type=ATTR, attr='src')

    author_name = retrieve(soup, 'span.author a[data-asin]')
    if author_name:
        author, created = Author.objects.get_or_create(name=author_name)

        author_link = retrieve(soup, 'a.contributorNameID', str_type=ATTR, attr='href')
        if author_link:
            author_link = 'http://www.amazon.com' + author_link
            bio, image = get_author_info(author_link)
            if created:
                if bio:
                    author.bio = bio
                if image:
                    author.image = image
                author.save()
    else:
        # Don't care about contributors (authors without a author profile on Amazon)
        return


    book, created = Book.objects.get_or_create(title=title, description=desc, author=author, price=price,
                rating=rating, image=book_image)
    book.save()
    book.tags.add(tag)

    print 'Scraped %s\n' % title



def get_author_info(url):
    response = requests.get(url, headers=HEADERS)
    soup = bs4.BeautifulSoup(response.text, 'lxml')

    bio = retrieve(soup, 'div#ap-bio span')
    image = retrieve(soup, '.ap-author-image', str_type=ATTR, attr='src')
    return bio, image

def scrape():
    KEYWORDS = [
        'python',
        'javascript',
        'css',
        'java',
        'go',
        'ruby',
        'clojure',
        'haskell',
        'ocaml',
    ]
    #  for keyword in cycle(KEYWORDS):
    for keyword in KEYWORDS:
        links = get_books_links(keyword=keyword)
        for book in links:
            get_book_data(book, keyword)
            time.sleep(30)
        time.sleep(30)