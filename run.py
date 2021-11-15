from selenium import webdriver
import os
from downloading import download

resp, chose = int(input('''[\033[1;32m1\033[m] \033[1;34mDownload a music\033[m
[\033[1;32m2\033[m] \033[1;34mDownload a list of musics\033[m
Answer: ''')), 0

os.system('cls' if os.name == 'nt' else 'clear')

output = int(input('''[\033[1;32m1\033[m] \033[1;34mDefine a directory \033[m
[\033[1;32m2\033[m] \033[1;34mDownload in current directory\033[m
Answer: '''))

if output == 1: output = input('\033[1;32mDirectory\033[m: ')
else: output = None

# DEFINING THE BROWSER AND GOING TO YOUTUBE
if resp == 1:
    music_name = input('\033[1;32mMusic name\033[m: ')
    music_name = music_name.replace(' ', '+')
    driver = webdriver.Chrome()
    driver.get(f"https://www.youtube.com/results?search_query={music_name}")

    # GETTING FIRST THE FIVE OCURRENCES.
    while not chose in range(1,6):
        for i in range(1, 6):
            video = driver.find_element_by_xpath(f'/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[1]/div/h3/a')
            if i == 1: os.system('cls' if os.name == 'nt' else 'clear')
            print(f'[\033[1;32m{i}\033[m] \033[1;34m{video.get_attribute("title")}\033[m')
        chose = int(input('Chose one of them: '))

    # CHOSING THE YT VIDEO AND GET ITS LINK, THEN DOWNLOADING IT WITH PYTUBE.
    video_chosed = driver.find_element_by_xpath(f'/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{chose}]/div[1]/div/div[1]/div/h3/a')
    download(video_chosed.get_attribute('href'), video_chosed.get_attribute('title'), output)
    driver.close()

else:
    music_names = list(input("\033[1;34mMusic Names\033[m \033[1;32m(Separe by using space)\033[m: ").split())
    print(music_names)

    driver = webdriver.Chrome()

    for i in music_names:
        driver.get(f"https://www.youtube.com/results?search_query={i}")
        video = driver.find_element_by_xpath(f'/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a')
        print(f"Downloading: \033[1;34m{video.get_attribute('title')}\033[m\n")
        download(video.get_attribute("href"), video.get_attribute('title'), output)