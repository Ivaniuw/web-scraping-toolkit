from bs4 import BeautifulSoup
import requests
import csv

url = "http://books.toscrape.com/"


response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all('article', class_='product_pod')

print("Books found:", len(books)) 

data = []
for page in range(1, 51):
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')
        


        for book in books:
            title = book.find('h3').find('a')['title']
            price = book.find('p', class_='price_color').get_text()
            rating = book.find('p', class_='star-rating')['class'][1]
            data.append({'title': title, 'price': price, 'rating': rating})
        
        print(f"Page {page}: collected {len(books)} books")
    
with open('books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'price', 'rating'])
    writer.writeheader()
    writer.writerows(data)
    
    
print('Save in books.csv')




