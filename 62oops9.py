#62
#multilevel inheritence

class Dad:
    basketball = 1

class Son(Dad):      #ye lega apne upar wale ka gunn
    dance = 1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son): #ye lega apne upar wale ka gunn
    dance = 6
    guitar = 1
    def isdance(self):
        return f"Jackson yeah" \
               f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()  #instances
larry = Son()
harry = Grandson()

print(harry.basketball) #pahle apne Gson me check akrega fir jisse inherit kiya hoga usme chech karegaSon fir Dad
print(harry.isdance())
# print(darry.guitar): E as no attribute guitar in darry nad nither Dad- place where it can inherit

#Quiz
#electronic device
#pocket gadget
#phone

class ed:
    def Ido(self):    #canot place space bw I and do
        playmusic = 3 #canot place space bw play and music
        navigation = 1
        camera = 1
        return
class pg(ed):
    def Ido(self):
        location = 2
        internet = 1
        apps = "2GB"
        return
class ph(pg):
    def Ido(self):
        call = 4
        sim = 2
        return
polldevice = ed()
lolgadget = pg()
myphone = ph()
print(myphone.Ido())









