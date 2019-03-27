import requests
import re
from bs4 import BeautifulSoup

def get_links(word):#リンクをリスト形式で返す．
	url = "https://en.oxforddictionaries.com/definition/{}".format(word)
	r = requests.get(url).text
	
	soup = BeautifulSoup(r, "lxml")
	tags = soup.find_all("audio")#tagsはaudioタグに囲まれた要素のリスト
	links = []
	for txt in tags:
		link = re.search('http.*.mp3', str(txt)).group()
		links.append(link)
	return links#[:-1]
if __name__ == '__main__':
	links = get_links("concur")
	print(links)
