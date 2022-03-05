from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

youtube_trending_url = "https://www.youtube.com/feed/trending"


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver
def get_videos():
  driver.get(youtube_trending_url)
  print('Page Title: ', driver.title)
  video_div_tag = 'ytd-video-renderer'
  videos = driver.find_elements(By.TAG_NAME, video_div_tag)
  return videos


if __name__ == '__main__':
    print("Geting Driver")
    driver = create_driver()
    print("Geting videos")
    videos = get_videos()
    print(f'Found {len(videos)} videos')

  # title, url, thumnail_url, channel, views, uploaded
    print("Parsing the first video")
  
  
  
    
    title_tag = driver.find_element(By.ID,'video-title')
    Title = title_tag.text
    print(f'Title: {Title}')
    
    URL = title_tag.get_attribute('href')
    print(f'URL: {URL}')

   
    thumbnail_img = driver.find_element(By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img')
    thumbnail_URL = thumbnail_img.get_attribute('src')
    print(f'Thumbnail Image URL: {thumbnail_URL}')
  
    channel_tag=driver.find_element(By.XPATH,'//yt-formatted-string[@id="text"]/a')
    channel_name = channel_tag.text
    channel_url = channel_tag.get_attribute('href')
    print(f'Channel Name: {channel_name}')
    print(f'Channel URL: https://www.youtube.com/{channel_url}')
  

          
  
 
    driver.quit()
