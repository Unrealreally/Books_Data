import requests
import re 
import pandas as pd
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/index.html"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

books_data = []


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


df = pd.DataFrame(books_data)
df.to_csv('books_data.csv', index=False)  # Save the DataFrame to a CSV file
df = pd.read_csv('books_data.csv')  # Read the CSV file back into a DataFrame
df['price'] = df['price'].astype(float)  # Ensure the 'price' column is of type float
df = df.sort_values(by='price', ascending=False)  # Sort the DataFrame by price in descending order
df = df.reset_index(drop=True)  # Reset the index after sorting

print(df)       
    

