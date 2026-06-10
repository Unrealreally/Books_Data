import requests
import re 
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/index.html"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

for book in soup.find_all('article', class_='product_pod'):

    title = book.find('h3').find('a')['title']
    print(title)    

    price_element = book.find('p', class_='price_color').text
    price = float(re.sub(r'[^\d.]', '', price_element)) # Remove the '£' symbol and convert to float
    print(price)

    rating_element = book.find('p', class_='star-rating')
    rating_classes = rating_element['class']
    rating = [cls for cls in rating_classes if cls != 'star-rating'][0]
    print(rating)

    availability_element = book.find('p', class_='instock availability')
    availability = availability_element.text.strip()
    print(availability)
    print()



