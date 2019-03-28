import pandas as pd

class ReadExcel:
	def __init__(self, i):
		self.df = pd.read_excel('book.xlsx',sheet_name=i)
	def GetNumber(self):
		return len(self.df)
	def SetWords(self, words_list):
		words = self.df["a"].values.tolist()
		wordsJp = self.df["b"].values.tolist()
		n = 0
		for one_word in words_list:
			one_word.Word = words[n]

			#set japanese word
			one_word.WordJp = wordsJp[n]

			one_word.Index= n
			n+=1




