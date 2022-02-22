from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

youtube_scraper_url="https://www.youtube.com/feed/trending"

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver=webdriver.Chrome(options=chrome_options)
  return driver

if __name__=="__main__":
  print('Creating Driver')
  driver=get_driver()

print("Fetching the page")
driver.get(youtube_scraper_url)

#driver.get("https://www.youtube.com/feed/trending")
#x=driver.find_element(By.XPATH,'//a[@class="yt-simple-endpoint style-scope ytd-video-renderer"]')
#print(x.text)

print('Get Video Divs')
Video_div_class='style-scope ytd-expanded-shelf-contents-renderer'
video_divs=driver.find_element(By.XPATH,'yt-simple-endpoint style-scope ytd-video-renderer')
print(video_divs)

print('Page Title using Selenium',driver.title)
