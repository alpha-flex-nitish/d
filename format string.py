
person = {'name':'jenn','age':'21'}

sentence = 'My name is ' + person['name'] +' and I am ' + person['age'] + ' years old.'

print(sentence)
# #1
person = {'name':'jenn','age':'21'}
sentencea = 'My name is '+person['name']+' and I am '+person['age']+' years old.'
print(sentencea)



# #2
person = {'name':'jenn','age':'21'}
sentenceb = 'My name is {} and I am {} years old.'.format(person['name'],person['age'])
print(sentenceb)



# #3
person = {'name':'jenn','age':'21'}
sentencec = 'My name is {0} and I am {1} years old.'.format(person['name'],person['age'])
print(sentencec)



# #3 a
numbers = {'don':'kaun','room':'groom','cent':'paint','wheat':'seat','Like':'BIKE'}

sentencen = 'Frst rhym is {0}, second rhym is {1}, third rhym is {2}, fourth rhym is {3}, fifth rhym' \
            ' is {4}.'.format\
              (numbers['don'],numbers['room'],numbers['cent'],numbers['wheat'],numbers['Like'])

print(sentencen)

sentencem = 'Frst rhym is {3}, second rhym is {2}, third rhym is {0}, fourth rhym is {4}, fifth rhym' \
            ' is {1}.'.format\
              (numbers['room'],numbers['room'],numbers['cent'],numbers['wheat'],numbers['Like'])
print(sentencem)



#  #4

tag = 'hi'
text = 'This is a headline'

sentenceD = '<{0}>{1}</{0}>'.format(tag,text)
sentennceD1 = '{0}{1}{0}'.format(text,tag)
print(sentenceD)
print("$",sentennceD1)
sentenceD2 = '<{0}>{1}<<0)$% ^&*($)%^&*{0}>'.format(tag,text)

print(sentenceD2)



# #5
    # Initially
person = {'name':'jenn','age':'21'}
sentencee = 'My name is {0} and I am {1} years old.'.format(person['name'],person['age'])
print(sentencee)
   #new tq
sentencee = 'My name is {0[name]} and I am {1[age]} years old.'.format(person,person)
print(sentencee)
sentencee = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentencee)



# #6

#our dictionary "person"

person = {'name':'senn','age':'21'}

l = ['jenn','23']

sentencef = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)

print(sentencef)
sentencef = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)

print(sentencef)


