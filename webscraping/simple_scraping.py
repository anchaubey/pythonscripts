import requests
from bs4 import BeautifulSoup

url = "https://www.dineout.co.in/delhi-restaurants/gurgaon/sector-54"

r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

links = soup.find_all("a")

g_data = soup.find_all("div", {"class": "listing-details"})

for item in g_data:
	print(item.text)

