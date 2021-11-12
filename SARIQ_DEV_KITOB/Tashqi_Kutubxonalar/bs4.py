
from bs4 import BeautifulSoup

sahifa = "https://kun.uz/news/main"


soup = BeautifulSoup('html.parser')
news = soup.find_all(class_='news-title')

print(news[0].soup)