import requests
from bs4 import BeautifulSoup


youtube_trending_url = "https://www.youtube.com/feed/trending"
# does not execute javascript
response = requests.get(youtube_trending_url)
print("Response Status Code: ", response.status_code)

with open('trending.html', 'w') as f:
  f.write(response.text)
doc = BeautifulSoup(response.text , 'html.parser')
print('Page Title: ',doc.title.text)

video_div = doc.find_all('div', class_ = "style-scope ytd-video-renderer")
print(f'Found {len(video_div)} trending videos on the page.')



#______________________________________________
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def get_videos(driver):
  video_div_tag = 'ytd-video-renderer'
  driver.get(youtube_trending_url)
  videos = driver.find_elements(By.TAG_NAME, video_div_tag)
  return videos
  
if __name__ == '__main__':
    print('Getting the driver')
    driver = get_driver()
    print(driver.title)
    #print("Fetching trending videos")
    #videos = get_videos(driver)

    #print(f'Found {len(videos)} videos on this page')

    driver.quit()