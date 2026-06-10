# Books Data App

A simple Streamlit dashboard for viewing and analyzing book data scraped from Books to Scrape.

## Features
- View the scraped book table
- Analyze the average price by rating
- Re-scrape data using the scraper script

## Run locally

Run these commands from the project root, which is the folder containing [README.md](README.md) and [requirements.txt](requirements.txt).

1. Install the required packages:
   pip install -r requirements.txt

2. Start the app:
   streamlit run src/app.py

## Project structure
- `src/app.py` — Streamlit dashboard
- `src/scrap.py` — scraper for updating the database
- `src/analysis.py` — analysis helper script
- `src/books.db` — SQLite database used by the app

## GitHub and Streamlit Cloud
1. Create a private GitHub repository on GitHub.
2. Upload this project to that repository.
3. In Streamlit Cloud, set the main file to `src/app.py`.

This project is ready for private use and for a first deployment test.
