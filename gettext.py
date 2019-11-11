import requests
from bs4 import BeautifulSoup

def findText(link):
    file = open("page.txt", "w")
    file.truncate()

    r = requests.get(link)

    soup = BeautifulSoup(r.text, from_encoding="UTF-8")
    text = str(soup.get_text())
    file.write(text)

findText("https://www.quora.com/For-whom-did-Jimmy-Wales-vote-in-the-2012-U-S-presidential-election")
