import pandas as pd

class ReadExcel:
	def __init__(self):
		self.i = i
	def GetWords(self, i):
		df = pd.read_excel('book.xlsx',sheet_name=self.i)
		words = df["a"].values.tolist()
		return words