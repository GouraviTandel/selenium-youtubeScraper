import pandas as pd
import requests
import time
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
  driver.implicitly_wait(30)
  driver.execute_script("window.scrollTo(0, 10000);")
  time.sleep(2)
  videos=driver.find_elements(By.TAG_NAME,Video_div_tag)
  return videos

def parse_video(video):
  title_tag=video.find_element(By.ID,'video-title')
  title=title_tag.text
  url=title_tag.get_attribute('href')
  thumbnail_imgtag=video.find_element(By.ID,'img')
  thumbnail_url=thumbnail_imgtag.get_attribute('src')
  Channel_tag=video.find_element(By.CLASS_NAME,'ytd-channel-name')
  Channel_name=Channel_tag.text
  description_text=video.find_element(By.ID,'description-text').text
  return {'title': title,
         'URL': url,
          'Thumbnail URL': thumbnail_url,
         'Thumbnail image src': thumbnail_imgtag,
         'Channel Name': Channel_name,
         'Description': description_text}

def send_email():
  pass
  
if __name__=="__main__":
  print('Creating Driver')
  driver=get_driver()
  print("Fetching Trending videos")
  videos=get_videos(driver)
  print("Found:",len(videos))

  print("Parsing Top 10 Videos")
  videosdata=[parse_video(i) for i in videos[:11]]
  #print(videosdata)
  print("save to CSV file")
  video_df=pd.DataFrame(videosdata)
  #print(video_df)
  video_df.to_csv('Trending_Video.csv')

  print('Send an email with the results')



