#50
#Healthy Programmer
#9am -5pm
#Water - water.mp3 (3.5 litres) - Drank - log
#Eyes - eyes.mp3 - every 30 min - EyDone - log
#Physical activity - physical.mp3 every - 45 min - ExDone - log
#
#Rules
#Pygame module to play audio


# from pygame import mixer
#
# def musiconloop(file, stopper):
# # def musiconloop('C:\Users\Nitish Shankar\Desktop', stopper)
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play(1000)
#     while True:
#         a = input()
#         if a == stopper:
#             mixer.music.stop()
#             break
# if __name__ == '__main__':
#     musiconloop('beep4.mp3','stop')

import time
localtime = time.asctime((time.localtime()))
print(localtime)
print(localtime[11:19:])

if (localtime[11:19:]=='19:58:00'):
    print('Drink jal')


    def musiconloop(file, stopper):
        mixer.init()
        mixer.music.load(file)
        mixer.music.play(1000)
        while True:
            a = input()
            if a == stopper:
                mixer.music.stop()
                break
    if __name__ == '__main__':
        musiconloop('beep4.mp3','stop')




# (localtime[11:19:]==(09:00:00))
while (localtime[11:19]<'17:00:00'):
    print("Drink water")
    time.sleep(4950)
    time.sleep(2)

    if (localtime[11:19]<'17:00:00'):
        break









