import sqlite3
import requests, re, pandas as pd
from bs4 import BeautifulSoup   
from urllib.parse import urljoin

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    price REAL, 
    rating TEXT,
    availability TEXT                                                                       
        
)''')

query = """SELECT rating,avg(price) AS average_price
 FROM books
 GROUP BY rating
 ORDER BY average_price DESC"""

url = "https://books.toscrape.com/index.html"
books_data = []

while True:
    page = requests.get(url)
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


print(f"Total books found: {len(books_data)}")
if len(books_data) > 0:
    print(f"Sample book: {books_data[0]}")  
else:
    print("Warning: No books were found. The loop might not be matching the HTML elements.")
    print(f"Current page URL: {url}")

df= pd.DataFrame(books_data)
df.to_sql('books', connection, if_exists='replace', index=False)   


query_result = connection.cursor().execute(query).fetchall()
top5books = pd.read_sql(query, connection)

print("Average price by rating:")
print(df.groupby('rating')['price'].mean().sort_values(ascending=False))
print(top5books)
connection.close()
