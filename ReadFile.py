import csv
from os import system


class ReadFile:
    words = []

    def _get_list(self):
        words = []
        with open('list.csv', 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                words.append(row[0])
        return words

    def __init__(self):
        words = self._get_list()


    def GetWords(self):
        return self.words

