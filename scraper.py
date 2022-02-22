import requests
from bs4 import BeautifulSoup

youtube_scraper_url="https://www.youtube.com/feed/trending"

response=requests.get(youtube_scraper_url)
print('Status Code:', response.status_code)
with open('trending.html','w') as f:
  f.write(response.text)

with open('trending.html','r') as f:
  html_source=f.read()
doc=BeautifulSoup(html_source,'html.parser')
print('title:',doc.title.text)

#Find all video Div 

video_divs=doc.find_all('div',class_="style-scope ytd-video-renderer")
print(video_divs)

