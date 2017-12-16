from __future__ import division
from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import urlopen
import threading

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

def threads():
    for _ in range(15):
        t = threading.Thread(target=work)
        t.start()

def get_data(url, index):
    try:
        html = urlopen(url).read()
        fi = open('/mnt/sda9/bookmark/news1/' + str(index) + '.txt', 'w')
        text = text_from_html(html)
        fi.write(text)
        fi.close()
    except:
        print('couldn\'t crawl : ' + url + '\n')

lock = threading.Lock()

def work():
    with open('/mnt/sda9/bookmark/parsed_data/news.txt') as f:
        index = 0
        for line in f:
            url = line.rstrip('\n')
            lock.acquire()
            try:
                index += 1
            finally:
                lock.release()
            get_data(url, index)
    f.close()

threads()