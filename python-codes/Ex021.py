'''abrir e reproduzir um audio mp3'''

from pygame import mixer
mixer.init()
mixer.music.load("ex021.mp3")
mixer.music.play()
input()
