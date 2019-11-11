import requests
from bs4 import BeautifulSoup
import threading
from collections import Counter

def textGetter(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.get_text()

file = open("Quotes.txt", "w")
link = "http://fortunes.herokuapp.com/random/raw"
text1 = textGetter(link)
quoteNum = 0
quoteList = Counter()

def recordQuotes():
    global text1
    global quoteNum
    global link
    global quoteList
    while (quoteList[text1] == 0):
        file.write(text1 + "\n\n")
        quoteList[text1] += 1
        print("So far, {} Quotes have been recorded.".format(quoteNum))
        text1 = textGetter(link);
        quoteNum += 1

t1 = threading.Thread(target=recordQuotes)
t2 = threading.Thread(target=recordQuotes)
t3 = threading.Thread(target=recordQuotes)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
