import requests
import re
from bs4 import BeautifulSoup
class UrlFetcher:
	def _get_one_word_link(self, one_word):
		url = "https://en.oxforddictionaries.com/definition/{}".format(one_word.Word)
		r = requests.get(url).text
		soup = BeautifulSoup(r, "lxml")
		tags = soup.find_all("audio")
		links = []
		for txt in tags:
			link = re.search('http.*.mp3', str(txt)).group()
			links.append(link)
		if(len(links)<2):
			one_word.HaveE = True
			print(one_word.Word)
			print(links)
			return None
		else:
			return links[0]
	def SetUrl(self, words_list):
		for one_word in words_list:
			one_word.Url = self._get_one_word_link(one_word)