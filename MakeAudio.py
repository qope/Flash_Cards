from os import system
from pydub import AudioSegment
import os
from mutagen.easyid3 import EasyID3

class MakeAudio:

    def _addSilent(self,oneWord):

        try:
            sound1 = AudioSegment.from_file(oneWord.AudioTempPath, "mp3")
            sound2 = AudioSegment.from_file("Silent3sec.mp3", "mp3")
            sound = sound1+sound2
            sound.export("words/{}_{}.mp3".format(str( oneWord.Index).zfill(4),oneWord.Word), format="mp3",bitrate="128k")
            print(">><((^ >")
        except:
            oneWord.HaveE = True
            print("error {}".format(oneWord.Word))
            print(">><((+ >")

    def MakeAudios(self,words):
        system("mkdir -p words")
        for word in words:
            if word.HaveE == False:
                self._addSilent(word)

    def ConnectAudio(self):
        system("mkdir -p conbined")

        index :int = 0
        files :str = os.listdir("words/")
        files.sort()
        i = 0

        while True:
            sound1 = None

            for j in range(30):
                sound2 = AudioSegment.from_file("words/{}".format(files[index]), "mp3")
                if sound1 == None : sound1 = sound2
                else :sound1 += sound2

                index+=1
                if index>=len(files):
                    sound1.export("conbined/test{}.mp3".format(i), format="mp3",bitrate="128k")
                    return
            sound1.export("conbined/test{}.mp3".format(i), format="mp3",bitrate="128k")
            i+=1

    def ConnectAudio2(self):
        system("mkdir -p conbined")

        files = os.listdir("words/")
        files.sort()
        j = 0
        k = 1
        N = 36
        while 1:
            sound = AudioSegment.from_file("words/{}".format(files[j]), "mp3")
            i = 0
            for file in files[j:]:
                if(i!=0 and i<N):
                    sound +=AudioSegment.from_file("words/{}".format(file), "mp3")
                i+=1
            sound.export("conbined/part{}.mp3".format(k), format="mp3",bitrate="128k")
            j+=N
            k+=1
            if(len(files)<=j):
                break

    def WriteAlbum(self):
        files = os.listdir("words/")
        files.sort()
        for file in files:
            path = "words/{}".format(file)
            tags = EasyID3(path)
            tags['album'] = 'words'
            tags['album'] = 'words'
            tags.save()

if __name__ == '__main__':
    m = MakeAudio()
    m.ConnectAudio2()
