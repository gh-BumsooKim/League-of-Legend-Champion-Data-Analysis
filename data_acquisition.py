from selenium import webdriver
import urllib.request
import os
import matplotlib.pyplot as plt

driver = webdriver.Chrome("./chromedriver.exe") # your chrome driver path
driver.get("https://universe.leagueoflegends.com/ko_KR/champions/")

image_list = driver.find_elements_by_css_selector('div.image_3oOd')

link = dict()

# Classic Image Download
for i, image in enumerate(image_list):
    url = image.get_attribute('data-am-url')
    back_align = image.get_attribute('style')
    
    # 'Champion Name' = [file_url, file_name, align_info]
    champ_name = url.split("/")[-1].split(".")[0]
    link[champ_name] = [url, url.split("/")[-1]] + back_align.split(" ")[3:5] #link[champ_name] = [url, back_align.split(" ")[3:5]]
    
    # Download Path
    if not os.path.isdir("champ_classic"):
        os.mkdir("champ_classic")
    
    # Image Download
    urllib.request.urlretrieve(url, "./champ_classic/" + str(i) + "_" + url.split("/")[-1])
    
    # Process Print
    print("Donwloaded {}/{} : {}".format(i+1, len(image_list), champ_name))

driver.close()
