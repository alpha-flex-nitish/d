#46
#f __name__==__main__ usage
def printhar(string):
    return f'Ye srting harry ko de de thakur{string}'
def add (num1, num2):
    return num1 + num2 +5



# print(printhar('Harry1'))
# o = add(4,6)
# # printhar(o)  NEO
# print(o)

print('and the name is',__name__)  # yaha par name ki value main hai
                                   # name ki value main tab hoti hai
                                   # jab aap usi programme ko run kar
                                   # rahe hai jisme apnme wo dala hua hai
#name ki value tutmain1 hogi agar aapisko kahi import karke chala rahe ho

if __name__ == '__main__':      # type'main' it will autosuggest the line
    print(printhar('Harry1'))
    o = add(4, 6)
    print(o)

#agar hum sirf 2nd last para run karte hai to tutmain2 me tutmain1 ke sare
#functions run honge but agar last para run karenge to tutmain1 ka content
#sirf yahi execute hoga naa ki jaha-jaha humne tutmain1 ko import kiya hai




#only next 2 lines in a code is useless
# l = add(4,6)
# print(l)


