import ReadExcel
import UrlFetcher
import DownLoad
import MakeAudio
# _read :ReadExcel.ReadExcel
# _urlf :UrlFetcher.UrlFetcher
# _dl :DownLoad.DownLoad
# _audio :MakeAudio.MakeAudio
class OneWord:

    def __init__(self):
        self.Url = ""
        self.Word = ""
        self.Index = 0
        self.AudioTempPath = ""
        self.AudioExportPath = ""
        self.HaveE = False

class Main:

    def _initWordsList(self,number):
        self._words = []
        for i in range(number):
            self._words.append(OneWord())

    def __init__(self):
        self._read = ReadExcel.ReadExcel(1)
        self._urlf = UrlFetcher.UrlFetcher()
        self._dl = DownLoad.DownLoad()
        self._audio = MakeAudio.MakeAudio()
        number = self._read.GetNumber()
        self._initWordsList(number)
        self._read.SetWords(self._words)
        self._urlf.SetUrl(self._words)
        self._dl.Download(self._words)
        self._audio.MakeAudios(self._words)
        self._audio.ConnectAudio2(30)


if __name__ == "__main__":
    _main = Main()






