import csv
from os import system
def download_mp3(num, word):
    system('curl -o words/{}_{}.mp3 https://ssl.gstatic.com/dictionary/static/sounds/oxford/{}--_gb_1.mp3'.format(str(num).zfill(4),word,word))
def get_list():
    words = []
    with open('list.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            words.append(row[0])
    return words
def add_silence(i):
    system('cp Silent3sec.mp3 words/{}.mp3'.format(str(i).zfill(4)))
words = get_list()
for i, word in enumerate(words):
    download_mp3(i*2, word)
    add_silence(i*2+1)
