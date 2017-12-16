from __future__ import division
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import glob

for z in glob.glob("/mnt/sda9/bookmark/videos/*"):
    file = open(z, 'r')
    # file = open("sports.txt", 'r')
    textt = file.read().lower()
    textt = re.sub("\d+", " ", textt)
    stemmer = PorterStemmer()
    print('opening file ' + z + '\n')
    if re.search('.*This is a message from the IT Department.*', textt):
        continue
    else:
        word1 = []
        tokenizer = RegexpTokenizer(r'\w+');
        word11 = tokenizer.tokenize(textt)
        for y in word11:
            wordd = stemmer.stem(y)
            word1.append(wordd)
        stop_words = set(stopwords.words("english"))
        # word1 = word_tokenize(text)
        word = [w for w in word1 if not w in stop_words]
        try:
            n = len(word)
            cv = TfidfVectorizer(min_df=1)
            x = cv.fit_transform(word)
            a = x.toarray()
            dict = {}
            idf = cv.idf_
            for i, j in zip(cv.get_feature_names(), idf):
                dict[i] = j
            score = []
            a = 0
            for j in word:
                if j in dict.keys():
                    a = a + dict[j]
                    score.append(a)
            score1 = [v for v in score]
            maxi = max(score1)
            j = 0
            for i in score1:
                score1[j] = i / maxi
                j = j + 1
            sent_dict = {}
            for i, j in zip(score1, word):
                sent_dict[i] = j
            sort_tot = sorted(score1)
            summary = []
            for i in range(len(sort_tot) - 20, len(sort_tot) - 1):
                if sent_dict[sort_tot[i]] not in summary:
                    summary.append(sent_dict[sort_tot[i]])
            with open('videos.txt', 'a') as f:
                for i in summary:
                    f.write(i + '\n')
            f.close()
        except:
            continue