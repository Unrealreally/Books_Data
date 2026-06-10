import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "books.db"


def load_data():
    connection = sqlite3.connect(DB_PATH)
    query = "SELECT * FROM books"
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df

df = load_data()

st.sidebar.title("Books Data App")
selected_option = st.sidebar.selectbox("Select an option", ["View Books Data", "Analyze Books Data"])

if selected_option == "View Books Data":
    st.title("Books Data")
    df = load_data()
    st.dataframe(df)
    
elif selected_option == "Analyze Books Data":
    st.title("Books Data Analysis")

    rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    connection = sqlite3.connect(DB_PATH)
    query = """SELECT rating, AVG(price) AS average_price
               FROM books
               GROUP BY rating
               ORDER BY average_price DESC"""
    
    analysis_df = pd.read_sql_query(query, connection)
    connection.close()

    st.write("Books Data:")
    st.dataframe(df)

    st.write("Average price of books by rating:")
    chart_data = analysis_df.groupby('rating')['average_price'].mean()
    st.bar_chart(chart_data)

    