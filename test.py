import ReadExcel
import UrlFetcher


class OneWord:
	def __init__(self):
		self.Index = 0
		self.Word = ""
		self.Url = ""
		self.HaveE = False

reader = ReadExcel.ReadExcel(1)
num = reader.GetNumber()
words_list = []
for i in range(num):
	word = OneWord()
	words_list.append(word)
reader.SetWords(words_list)
urlfet = UrlFetcher.UrlFetcher()
urlfet.SetUrl(words_list)
for one_word in words_list:
	print(one_word.Word)
			