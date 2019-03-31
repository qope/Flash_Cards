import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver

word ="run-off"
url = "https://en.oxforddictionaries.com/definition/{}".format(word)
r = requests.get(url,timeout=2, headers = {"User-Agent": "hoge"}).text
soup = BeautifulSoup(r, "lxml")
tags = soup.find_all("audio")
links = []
for txt in tags:
	link = re.search('http.*.mp3', str(txt)).group()
	links.append(link)
print(links)