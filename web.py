from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re


httpObject = urlopen("https://www.flipkart.com/search?q=best+laptop+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY")

webdata = httpObject.read()
soup1 = soup(webdata)
pages_link = soup1.findAll('a', {'class':'ge-49M'})
domain=('https://www.flipkart.com/search?q=best+laptop+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page=')


for i in range(2, 50):
    link = domain + str(i)
    page_data = urlopen(link)
    webdata1 = page_data.read()
    webdata += webdata1

soupdata = soup(webdata, 'html.parser')

containers = soupdata.findAll('div', {'class':'_2kHMtA'})
f = open('laptop info.csv', 'wb')   
f.write('productname,Stars,Ratings,Reviews,CurrentPrice,processor,Ram,Storage,ImageUrl\n'.encode())

for container in containers:
    product = container.find('div', {'class':'_4rR01T'})
    productname = product.text.split('-')[0]

    star = container.find('div', {'class':'_3LWZlK'})
    try:
        Stars = star.text
    except:
        Stars = 0

    Rating = container.find('span', {'class':'_2_R_DZ'})

    try:
        ratrev = re.findall('\d+,?\d*', Rating.text)
        Ratings = ratrev[0].replace(',', '')
        Reviews = ratrev[1].replace(',', '')
    except:
        Ratings = 0

    CurrentPrice = container.find('div', {'class':'_30jeq3 _1_WHN1'})
    try:
        currentprice = CurrentPrice.text.replace(',', '')
    except:
        currentprice = 0

    info = container.findAll('li', {'class':'rgWa7D'})
    processor = info[0].text
    Ram = info[1].text
    Storage = info[3].text
    Image = container.img
    ImageUrl = Image.get('src')

    print(productname, Stars, Ratings, Reviews, CurrentPrice, processor, Ram, Storage, ImageUrl) 

    f.write(f"{productname},{Stars},{Ratings},{Reviews},{currentprice},{processor},{Ram},{Storage},{ImageUrl}\n".encode())

print('\n')
f.close()



