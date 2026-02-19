# Product Scraper

A Python CLI app that scrapes product data from web-scraping.dev,
stores it in PostgreSQL, and exports to CSV or JSON.

## Features
- Scrapes product name, description, price
- Stores data in PostgreSQL database
- Exports to CSV or JSON via CLI menu
- Full error handling throughout

## Setup
1. Clone the repo
2. Create virtual environment: python -m venv .venv
3. Activate it
4. Install libraries: pip install -r requirements.txt
5. Set your PostgreSQL password in database.py
6. Run: python main.py

## Libraries Used
- requests
- beautifulsoup4
- psycopg2-binary