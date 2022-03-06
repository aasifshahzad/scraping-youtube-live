from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import csv

youtube_trending_url = "https://www.youtube.com/feed/trending"


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver
def get_videos(driver):
  driver.get(youtube_trending_url)
  print('Page Title: ', driver.title)
  video_div_tag = 'ytd-video-renderer'
  videos = driver.find_elements(By.TAG_NAME, video_div_tag)
  return videos

def parse_videos(video):
  title_tag = video.find_element(By.ID,'video-title')
  Title = title_tag.text
  URL = title_tag.get_attribute('href')
  thumbnail_img = video.find_element(By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img')
  thumbnail_URL = thumbnail_img.get_attribute('src')
  channel_tag=video.find_element(By.XPATH,'//yt-formatted-string[@id="text"]/a')
  channel_name = channel_tag.text
  channel_url = channel_tag.get_attribute('href')
  views_time_xpath =('//div[@id="metadata-line"]' and '//div[@class="style-scope ytd-video-meta-block"]')
  views_time_tag = video.find_element(By.XPATH, views_time_xpath)
  views_time_text = views_time_tag.text.split()
  views = ' '.join(views_time_text[1:3])
  upload_time = ' '.join(views_time_text[3:6])
  video_discription_tag =    video.find_element(By.XPATH, '//yt-formatted-string[@id="description-text" and @class="style-scope ytd-video-renderer" ]')
  video_discription_text =    video_discription_tag.text
  return {
    'Title' : Title,
    'URL' : URL,
    #'Thumbnail_Image' : thumbnail_img,
    'Thumbnail_URL' : thumbnail_URL,
    'Channel_Name' : channel_name,
    'Channel_URL' : channel_url,
    'Views' : views,
    'Upload_since' : upload_time,
    'Discription' : video_discription_text,
     }
  
if __name__ == '__main__':
    print("Geting Driver")
    driver = create_driver()
    print("Geting videos")
    videos = get_videos(driver)
    print(f'Found {len(videos)} videos')

  # title, url, thumnail_url, channel, views, uploaded
    print("Parsing the top 10 videos")
    videos_data = [parse_videos(video)for video in videos[:10]]
    print("Save Video Data to CSV")
    videos_df = pd.DataFrame(videos_data)
    print(videos_df)
    videos_df.to_csv('youtube_trending.csv', index= None)

    driver.quit()
