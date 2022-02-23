
import requests
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

def get_videos(driver):
  driver.get(youtube_scraper_url)
  Video_div_tag='ytd-video-renderer'
  driver.implicitly_wait(20)
  videos=driver.find_elements(By.CLASS_NAME,Video_div_tag)
  return videos
  
if __name__=="__main__":
  print('Creating Driver')
  driver=get_driver()
  print("Fetching Trending videos")
  videos=get_videos(driver)
  print("Found:",len(videos))

print("Parsing 1st Video")