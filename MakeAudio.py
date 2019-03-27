from os import system
from pydub import AudioSegment
import os

class MakeAudio:

    # def _wordAudio(self,oneWord):
    #     try:
            
    #     except:
    #         oneWord.HaveE = True
    #         print(oneWord.Word)



    def _addSilent(self,oneWord):

        try:
            sound1 = AudioSegment.from_file(oneWord.AudioTempPath, "mp3")
            sound2 = AudioSegment.from_file("Silent3sec.mp3", "mp3")
            sound = sound1+sound2
            sound.export("words/{}_{}.mp3".format(str( oneWord.Index).zfill(4),oneWord.Word), format="mp3")
        except:
            oneWord.HaveE = True
            print("error {}".format(oneWord.Word))

    

    def MakeAudios(self,words):
        for word in words:
            if word.HaveE == False:
                # self._wordAudio(word)
                self._addSilent(word)
                print(">><((^ >")


    def ConnectAudio(self):
        index :int = 0

        files :str = os.listdir("words/")
        files.sort()

        while True:

            sound = AudioSegment.from_file("words/{}".format(files[index]), "mp3")
            index += 1

            for j in range(34):
                sound1 = AudioSegment.from_file("words/{}".format(files[index]), "mp3")

                sound+sound1

                index+=1
                if index>=len(files):break

                









          
    
