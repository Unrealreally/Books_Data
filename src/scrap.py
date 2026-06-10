import requests, sqlite3
import re
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "books.db"


def scrape_books():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY, 
        title TEXT,
        price REAL, 
        rating TEXT,
        availability TEXT   
                   
    )''')

    url = "https://books.toscrape.com/index.html"
    books_data = []

    while True:
        page = requests.get(url, timeout=30)
        soup = BeautifulSoup(page.text, 'html.parser')

        for book in soup.find_all('article', class_='product_pod'):
            title = book.find('h3').find('a')['title']

            price_element = book.find('p', class_='price_color').text
            price = float(re.sub(r'[^\d.]', '', price_element)) # Remove the '£' symbol and convert to float

            rating_element = book.find('p', class_='star-rating')
            rating_classes = rating_element['class']
            rating = [cls for cls in rating_classes if cls != 'star-rating'][0]

            availability_element = book.find('p', class_='instock availability')
            availability = availability_element.text.strip()

            booksinfo = {
                'title': title,
                'price': price,
                'rating': rating,
                'availability': availability
            }

            books_data.append(booksinfo)

        next_page = soup.find('li', class_='next')
        if next_page:
            next_url = next_page.find('a')['href']
            url = urljoin(url, next_url)  # Construct the full URL for the next page
        else:
            break

    for book in books_data:
        cursor.execute('''INSERT OR REPLACE INTO books (title, price, rating, availability) VALUES (?, ?, ?, ?)''', 
                       (book['title'], book['price'], book['rating'], book['availability']))

    connection.commit()
    connection.close()

print("Done! books.db updated with scraped data.")
if __name__ == "__main__":
    scrape_books()