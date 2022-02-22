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

print('Get Video Divs')
Video_div_tag='ytd-video-renderer'
video_divs=driver.find_elements_by_tag_name(Video_div_tag)
print(video_divs)

print('Page Title using Selenium',driver.title)
