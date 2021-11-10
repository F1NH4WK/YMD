from selenium import webdriver
from time import sleep
import selenium
from selenium.webdriver.common.keys import Keys
import os
from downloading import download

music_name = input('Music name: ')

# DEFINING THE BROWSER AND GOING TO YOUTUBE
driver = webdriver.Chrome()
driver.get("https://www.youtube.com")

# FINDING THE SEARCH INPUT BY XPATH AND SEARCHING.
element = driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
element.send_keys(music_name)

# USING SLEEP TO NOT END THE PROGRAM BY TIMEOUT
sleep(3)
element.send_keys(Keys.ENTER)
sleep(3)

#GETTING FIRST FIVE OCURRENCES.
for i in range(1, 6):
    video = driver.find_element_by_xpath(f'/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[1]/div/h3/a')
    if i == 1: os.system('cls' if os.name == 'nt' else 'clear')
    print(f'[\033[1;32m{i}\033[m] Video: \033[1;34m{video.get_attribute("title")}\033[m')

chose = int(input("Chose one of them: "))
video_chosed = driver.find_element_by_xpath(f'/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{chose}]/div[1]/div/div[1]/div/h3/a')
download(video_chosed.get_attribute('href'), input("Name of archive: "))
driver.close()