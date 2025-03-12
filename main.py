#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
# Google Chrome Driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyWidget(BoxLayout):
    # Set up Google Chrome driver
    driver = webdriver.Chrome()
    # Manually change the URL of the webpage where the video you want to download is located
    url = 'https://www.netflix.com/video/1529-1-1.html'

# open the Web page
driver.get(url)

try:
    # Find the iframe through the element selector
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,'#playleft iframe'))
    )
except:
    driver.quit()

# Get the title of the webpage, so that you can visually see the title of the currently downloaded video
title = driver.find_elements(By.TAG_NAME,'title')[
    0].get_attribute('innerHTML')

# Switch to iframe
driver.switch_to.frame(iframe)

# Get the video address through the video tag
video = driver.find_elements(By.TAG_NAME,'video')[0]
video_url = video.get_attribute('src')
print('video', video_url)

# The video address has been obtained, you can close the browser
driver.quit()

# Set request header information
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}

# Request video content
video_content = requests.get(video_url, headers=headers, stream=True)

print("Start downloading")

# Video size
contentLength = int(video_content.headers['content-length'])

line ='Size: %.2fMB'

# Size conversion
line = line % (contentLength/1024/1024)

# Print the total length of the video
print(line)

# Store the downloaded length
downSize = 0

print('video_name', title)

# Fragmented download
with open(title+'.mp4', "wb") as mp4:
    for chunk in video_content.iter_content(chunk_size=1024 * 1024):
        if chunk:
            mp4.write(chunk)

            # Record the length of the downloaded video and output the download progress in real time
            downSize += len(chunk)
            print('Progress: {:.2%}'.format(downSize / contentLength), end='\r')
            print("download end")
    
    class VidDwnApp(App):
        def build(self):
            return MyWidget()

    if __name__ == "__main__":
        VidDwnApp().run()
