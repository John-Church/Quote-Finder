import requests
from bs4 import BeautifulSoup
import threading
from collections import Counter

def textGetter(link):
    '''
    Returns all the text from a wepage of a given link.
    '''
    r = requests.get(link)
    # grabs web content as BeautifulSoup object
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.get_text()  # returns all text from web content

file = open("Quotes.txt", "w")  # opens/ creates new text file to record quotes
link = "http://fortunes.herokuapp.com/random/raw"   # link to parse
text1 = textGetter(link)
quoteNum = 0
quoteList = Counter()   # python counter (dict subclass that counts # of times
                        # an item has been recorded)

def recordQuotes():
    # Globals needed for threading
    global text1
    global quoteNum
    global link
    global quoteList
    while (quoteList[text1] == 0): # iterate while quote hasn't been counted yet
        file.write(text1 + "\n\n")
        quoteList[text1] += 1 # count quote
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
