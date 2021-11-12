import requests  
import os
os.path

from wordcloud import WordCloud

from bs4 import BeautifulSoup

import matplotlib.pyplot as plt


sahifa = "https://kun.uz/news/main"

r=requests.get(sahifa)



soup = BeautifulSoup(r.text,'html.parser')
news = soup.find_all(class_="news-title")

matn = " "


for n in news:
  matn += n.text


wordcloud = WordCloud(width=100, height=1000,background_color = "white",min_font_size=20).generate(matn)




plt.figure(figsize = (8,8),facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
