import csv
from os import system
from pydub import AudioSegment
import MakeAudio



class OneWord:

    def __init__(self):
        self.Url = "https://s3.amazonaws.com/audio.oxforddictionaries.com/en/mp3/pronunciation_gb_1_8.mp3"
        self.Word = "pronunciation"
        self.Index = 0
        self.Audio = None
        self.AudioTempPath = ""
        self.AudioExportPath = ""
        self.HaveE = False


class DownLoad:
    def _download_mp3(self,word):
        try:
            path = "pre_words/{}.mp3".format(word.Word)
            system("curl -o {} {}".format(path,word.Url))
            word.AudioTempPath = path
        except:
            word.HaveE = True
            
            

    def Download(self,words:list):
        for i in range(len(words)):
            word = words[i]
            if word.HaveE == False:
                self._download_mp3(word)
                



if __name__ == "__main__":
    wos = [OneWord()]
    d = DownLoad()
    d.Download(wos)
    m = MakeAudio.MakeAudio()
    m.MakeAudios(wos)