from os import system
from pydub import AudioSegment
import MakeAudio

class DownLoad:
    def _download_mp3(self,word):
        try:
            path = "pre_words/{}.mp3".format(word.Word)
            system("curl -o {} {}".format(path,word.Url))
            word.AudioTempPath = path
        except:
            word.HaveE = True
            print("error {}".format(word.Word))
    def Download(self,words:list):
        system("mkdir -p pre_words")
        for word in words:
            if word.HaveE == False:
                self._download_mp3(word)

if __name__ == "__main__":
    wos = [OneWord(),OneWord2()]
    d = DownLoad()
    d.Download(wos)
    m = MakeAudio.MakeAudio()
    m.MakeAudios(wos)
    m.ConnectAudio()