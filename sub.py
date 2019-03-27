import requests
import re
from bs4 import BeautifulSoup
<<<<<<< HEAD


class DownloadMp3:
	# def _get_links(self,word):#リンクをリスト形式で返す．
	# 	url = "https://en.oxforddictionaries.com/definition/{}".format(word)
	# 	r = requests.get(url).text
		
	# 	soup = BeautifulSoup(r, "lxml")
	# 	tags = soup.find_all("audio")#tagsはaudioタグに囲まれた要素のリスト
	# 	links = []
	# 	for txt in tags:
	# 		link = re.search('http.*.mp3', str(txt)).group()
	# 		links.append(link)
	# 	return links[:-1]


	def GetMp3(self,oneWord):
		links = self._get_links(oneWord.Word)
		oneWord.AudioTempPath = links
		print(links)



=======
def get_links(word):#リンクをリスト形式で返す．
	url = "https://en.oxforddictionaries.com/definition/{}".format(word)
	r = requests.get(url).text
	soup = BeautifulSoup(r, "lxml")
	tags = soup.find_all("audio")#tagsはaudioタグに囲まれた要素のリスト
	links = []
	for txt in tags:
		link = re.search('http.*.mp3', str(txt)).group()
		links.append(link)
	return links
if __name__ == '__main__':
	links = get_links("runoff")
	print(links)
>>>>>>> 26416aded1159974d72aa7449c9ab5a47b768547
