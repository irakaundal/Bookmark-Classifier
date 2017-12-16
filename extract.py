from __future__ import division
from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.request import urlopen
import threading

file = ['sports.txt','education.txt', 'entertainment.txt', 'news.txt', 'songs.txt', 'videos.txt']
cat = ['sports', 'education', 'entertainment', 'news', 'songs', 'videos']

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
    threading.Thread(target=extract1).start()
    threading.Thread(target=extract2).start()
    threading.Thread(target=extract3).start()
    threading.Thread(target=extract4).start()
    threading.Thread(target=extract5).start()
    threading.Thread(target=extract6).start()

def get_data(url, index, which):
    try:
        html = urlopen(url).read()
        fi = open('/mnt/sda9/bookmark/' + cat[which-1] + '/' + str(index) + '.txt', 'w')
        text = text_from_html(html)
        fi.write(text)
        fi.close()
    except:
        print('couldn\'t crawl : ' + url + '\n')

def extract1():
    x = file[0]
    with open('/mnt/sda9/bookmark/parsed_data/' + x) as f:
        index = 0
        for line in f:
            url = line.rstrip('\n')
            index += 1
            get_data(url, index, 1)
    f.close()

def extract2():
    x = file[1]
    with open('/mnt/sda9/bookmark/parsed_data/' + x) as f:
        index = 0
        for line in f:
            url = line.rstrip('\n')
            index += 1
            get_data(url, index, 2)
    f.close()

def extract3():
    x = file[2]
    with open('/mnt/sda9/bookmark/parsed_data/' + x) as f:
        index = 0
        for line in f:
            url = line.rstrip('\n')
            index += 1
            get_data(url, index, 3)
    f.close()

def extract4():
    x = file[3]
    with open('/mnt/sda9/bookmark/parsed_data/' + x) as f:
        index = 0
        for line in f:
            url = line.rstrip('\n')
            index += 1
            q
    f.close()

def extract5():
    x = file[4]
    with open('/mnt/sda9/bookmark/parsed_data/' + x) as f:
        index = 0
        for line in f:
            url = line.rstrip('\n')
            index += 1
            get_data(url, index, 5)
    f.close()

def extract6():
    x = file[5]
    with open('/mnt/sda9/bookmark/parsed_data/' + x) as f:
        index = 0
        for line in f:
            url = line.rstrip('\n')
            index += 1
            get_data(url, index, 6)
    f.close()

threads()

