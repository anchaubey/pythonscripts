import requests
from bs4 import BeautifulSoup
import urllib
import os


os.chdir('C:\\Users\\E211568\\Desktop\\images')

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

i = 1

soup = make_soup("https://www.jabong.com/men-formal-shirts")
for img in soup.findAll('img'):
    temp=img.get('data-src')
    if temp[:1]=="/":
        image = "https://www.jabong.com/men-formal-shirts" + temp
    else:
        image = temp


    nametemp = img.get('alt')
    if str(nametemp)=='None':
        filename=str(i)
        i = i + 1
    else:
        filename=nametemp
    
    imagefile = open(filename + ".jpeg","wb")
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()
