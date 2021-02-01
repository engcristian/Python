'''
Playing a mp3 using the mixer from pygame lib
'''
from pygame import mixer
mixer.init()
mixer.music.load("music.mp3")
mixer.music.play()
input()
