# web-scraping-toolkit
Python web scrapers for static and dynamic sites — requests/BeautifulSoup for server-rendered pages, Playwright for JavaScript-loaded content. Handles pagination and exports clean CSV.

Two Python scrapers demonstrating both static and dynamic web scraping approaches.

## Projects

### 1. Static Scraper — `books.py`

Scrapes a full product catalog using `requests` + `BeautifulSoup`.

**Features:**
- Extracts title, price, and rating for each product
- Handles pagination across all catalog pages (~1000 records)
- UTF-8 encoding handling for special characters
- Rate limiting between requests
- Exports clean data to CSV

**Run:**
pip install requests beautifulsoup4
python books.py


### 2. Dynamic Scraper — `pw_books.py`

Scrapes the same site through a real browser using **Playwright**, navigating by clicking pagination links instead of constructing URLs.

**Features:**
- Controls a real Chromium browser (headless or visible)
- Navigates by clicking "next" — works on sites where URLs aren't predictable
- Extracts data from fully rendered HTML (handles JavaScript-loaded content)
- Combines Playwright for navigation with BeautifulSoup for parsing
- Exports to CSV

**Run:**
pip install playwright beautifulsoup4
python -m playwright install
python pw_books.py


## Why two approaches

`requests` is fast and lightweight but only sees the raw HTML returned by the server. Many modern sites render their content with JavaScript, leaving that HTML nearly empty. Playwright loads the page in a real browser, waits for content to render, and returns the complete HTML — at the cost of being slower and heavier.

Rule of thumb: use `requests` when the data is in the page source, use Playwright when it isn't.

## Tech

Python 3 · requests · BeautifulSoup4 · Playwright · csv

## Note

Both scripts target [books.toscrape.com](http://books.toscrape.com/), a site built specifically for scraping practice. Always check a site's Terms of Service and `robots.txt` before scraping.
