import ReadExcel
import UrlFetcher
import DownLoad
import MakeAudio

class OneWord:

    def __init__(self):
        self.Url = ""
        self.Word = ""
        self.Index = 0
        
        self.AudioTempPath = ""
        self.AudioExportPath = ""
        self.HaveE = False

class Main:

    _words = []

    def _initWordsList(self,number):
        for i in range(number):
            self._words.append(OneWord())

    def __init__(self):
        self._read = ReadExcel.ReadExcel(3)
        self._urlf = UrlFetcher.UrlFetcher()
        self._dl = DownLoad.DownLoad()
        self._audio = MakeAudio.MakeAudio()

        number :int = self._read.GetNumber()
        self._initWordsList(number)
        self._read.SetWords(self._words)
        self._urlf.SetUrl(self._words)

        self._dl.Download(self._words)
        self._audio.MakeAudios(self._words)
        self._audio.ConnectAudio2()
        self._audio.WriteAlbum()

if __name__ == "__main__":
    _main = Main()






