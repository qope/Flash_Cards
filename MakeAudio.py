from os import system
from pydub import AudioSegment

class MakeAudio:

    def _wordAudio(self,oneWord):
        try:
            oneWord.Audio = AudioSegment.from_file(oneWord.AudioTempPath, "mp3")
        except:
            oneWord.HaveE = True
            print("音声探しエラーだよ")



    def _addSilent(self,oneWord):

        try:
            sound2 = AudioSegment.from_file("Silent3sec.mp3", "mp3")
            sound = oneWord.Audio+sound2
            sound.export("words/{}_{}.mp3".format(oneWord.Index,oneWord.Word), format="mp3")
        except:
            oneWord.HaveE = True
            print("音声合成エラーだよ")

    

    def MakeAudios(self,words):
        for i in range(len(words)):
            word = words[i]
            if word.HaveE == False:
                self._wordAudio(word)
                self._addSilent(word)
          
    
