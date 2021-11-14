from selenium import webdriver
import os
from downloading import download

music_name = input('Music name: ')
music_name = music_name.replace(' ', '+')
chose = 0

# DEFINING THE BROWSER AND GOING TO YOUTUBE
driver = webdriver.Chrome()
driver.get(f"https://www.youtube.com/results?search_query={music_name}")

#GETTING FIRST FIVE OCURRENCES.
while not chose in range(1,6):
    for i in range(1, 6):
        video = driver.find_element_by_xpath(f'/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[1]/div/h3/a')
        if i == 1: os.system('cls' if os.name == 'nt' else 'clear')
        print(f'[\033[1;32m{i}\033[m] Video: \033[1;34m{video.get_attribute("title")}\033[m')
    chose = int(input("Chose one of them: "))

video_chosed = driver.find_element_by_xpath(f'/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{chose}]/div[1]/div/div[1]/div/h3/a')
download(video_chosed.get_attribute('href'), video_chosed.get_attribute('title'))

driver.close()