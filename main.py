import requests
from bs4 import BeautifulSoup


url = "https://books.toscrape.com/catalogue/the-stranger_861/index.html"



page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


title_element = soup.find('h1')
print(title_element.text)


price_element = soup.find('p', class_='price_color')
print(price_element.text)


rating_element = soup.find('p', class_='star-rating')

print(rating_element['class'][1])


availability_element = soup.find('p', class_= 'instock availability')

print(availability_element.text.strip())
