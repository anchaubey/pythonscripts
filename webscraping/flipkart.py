from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re

my_url = "https://www.flipkart.com/search?q=iphone&marketplace=FLIPKART&otracker=start&as-show=on&as=off"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')
containers = page_soup.findAll("div", {"class": "_3O0U0u"})
print(len(containers))

#print(soup.prettify(containers[0]))

container = containers[0]
print(container.div.img["alt"])

price=container.findAll("div", {"class":"_3auQ3N _2GcJzG"})
print(price[0].text)

display=container.findAll("div", {"class":"_3ULzGw"})
print(display[0].text)


rating=container.findAll("div", {"class":"niH0FQ"})
rated = rating[0].text
pattern = r'\d\.\d'
print("Rating:", re.findall(pattern,rated)[0])

filename="C:\\Users\\E211568\\Desktop\\flipkart1.csv"
f = open(filename, "w")

headers="Product_name,Pricing(In Rs.),Ratings\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]
    try:
        price_container = container.findAll("div", {"class":"_3auQ3N _2GcJzG"})
        price = price_container[0].text.split("₹")[1]
    except IndexError as e:
        pass
    rating_container = container.findAll("div", {"class":"niH0FQ"})
    rating = rating_container[0].text


    print("product_name: " + product_name)
    print("price: " + price)
    print("ratings: " + rating)

    split_rating = rating.split(" ")
    final_rating = split_rating[0]

    f.write(product_name.replace(",", "|") + "," + price.replace(",", " ") + "," + final_rating + "\n")
f.close()
