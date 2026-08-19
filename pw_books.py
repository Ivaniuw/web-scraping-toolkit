from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv

data = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("http://books.toscrape.com/")

    for i in range(5):
        html = page.content()
        soup = BeautifulSoup(html, "html.parser")
        books = soup.find_all('article', class_='product_pod')

        for book in books:
            title = book.find('h3').find('a')['title']
            price = book.find('p', class_='price_color').get_text()
            data.append({'title': title, 'price': price})

        print(f"Page {i+1}: scraped {len(books)} books")
        page.click("a:has-text('next')")

    browser.close()

with open('books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'price'])
    writer.writeheader()
    writer.writerows(data)

print(f"Saved {len(data)} records to books.csv")