c = 1
print("Guess A Number 5 chances left")

num = int(input())
while(c<6):
    if (num == 18):
        print('you guessed the correct number. You took',c,'chances')
        break
    c = c + 1
    if (c == 6):
        print("G.O.You used 5 chances try again")
        break
    if (num >= 0 and num < 10):
        print('you are far less')
    if (num >= 10 and num < 15):
        print('you are little less')
    if (num >= 15 and num < 18):
        print('you are but very close')
    if (num > 18 and num < 22):
        print('you are more but very close')
    if (num >= 22 and num < 26):
        print('you are little more')
    if (num >= 26 and num <= 36):
        print('you are far more')
    if (num >= 36 and num <= 50):
        print('you are far far more')
    if (num >50):
        print('input error')
    print('Guess A Number', 6-c ,'chances left')
    num = int(input())

   # if (c == 6):
    #    print("You used 5 chances try again")
     #   break



   # if(c==5):
    #    break










'''#while (chance<=5):
else:
        print('you guessed in rightly in', cahnce, 'cahnce')

#       break:
      #  chance = chance + 1
'''




