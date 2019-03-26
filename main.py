import csv
from os import system
from pydub import AudioSegment
def download_mp3(num, word):
    system('curl -o pre_words/{}.mp3 https://ssl.gstatic.com/dictionary/static/sounds/oxford/{}--_gb_1.mp3'.format(word,word))
    sound1 = AudioSegment.from_file("pre_words/{}.mp3".format(word), "mp3")
    sound2 = AudioSegment.from_file("Silent3sec.mp3", "mp3")
    sound = sound1+sound2
    sound.export("words/{}_{}.mp3".format(num,word), format="mp3")
def get_list():
    words = []
    with open('list.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            words.append(row[0])
    return words

words = get_list()
for i, word in enumerate(words):
    download_mp3(i, word)