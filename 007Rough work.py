#audiomixer
import pygame
import time
print(1)
print("-")
# pygame.mixer.music.pause()
print("-")
print(2)
file = 'C:\\Users\\Nitish Shankar\\PycharmProjects\\pythonTuts\\audio\\smallmusic.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
time.sleep(10)
print(3)
pygame.mixer.music.pause()
# time.sleep(1)
print(4)
# pygame.mixer.music.play()
# time.sleep(5)
pygame.mixer.music.unpause()
time.sleep(20)
print(5)





















