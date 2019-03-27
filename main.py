import ReadExcel
import UrlFecher
import DownLoad
import MakeAudio


_read :ReadExcel.ReadExcel
_urlf :UrlFecher.UrlFecher
_dl :DownLoad.DownLoad
_audio :MakeAudio.MakeAudio



class Main:

    _words = []

    def _initWordsList(self,number):
        for i in range(number):
            self._words.append(OneWord())


    def _initialize(self):
        _read = ReadExcel.ReadExcel()
        _urlf = UrlFecher.UrlFecher()
        _dl = DownLoad.DownLoad()
        _audio = MakeAudio.MakeAudio()


    def __init__(self):
        self._initialize()
        number :int = _read.GetNumber()
        self._initWordsList(number)
        _read.GetWords(number)
        _urlf.SetUrl(self._words)



        _dl.GetMp3(self._words)
        _audio.MakeAudios(self._words)



if __name__ == "__main__":
    _main = Main()


class OneWord:

    def __init__(self):
        self.Url = ""
        self.Word = ""
        self.Index = 0
        self.Audio = None
        self.AudioTempPath = ""
        self.AudioExportPath = ""
        self.HaveE = False



