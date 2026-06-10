import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "books.db"


def analyze_books():
    connection = sqlite3.connect(DB_PATH)
    query = """SELECT rating, AVG(price) AS average_price
               FROM books
               GROUP BY rating
               ORDER BY average_price DESC"""
    
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df

if __name__ == "__main__":
    analyze_books()