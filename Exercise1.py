#Create a dictionary and take input from user and return the meaning of the word
#from the dictionary

d1 = {'goat':'bakri','lion':'ser','tiger':'bagh','cow':'gaai'}
d2 = {'goat':'webgoat','lion':'weblion','tiger':'webtiger','cow':'webcow'}

print('enter a word')
inpword = input()
print('Meaning of',inpword,'is',d1[inpword]+'.','Get more information on',inpword,'from:'+d2[inpword]+'.com')
#print(d1[inpword])
#print('Meaning of'+('inpword')+'is'+d1['inpword'] )

