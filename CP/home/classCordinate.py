class Cordinate(object):
    
    def __init__(self,x,y):
        self.x=x
        self.y=y

   #mit in python feel

   # def distance(C1,C2):
   #     d=((C1.x-C2.x)**2+(C1.y-C2.y)**2)**(1/2)
   #     return di

   # me in java  feel
    def distance(self,c):
        d=((self.x-c.x)**2+(self.y-c.y)**2)**(0.5)
        return d
    def __str__(self):
        return '<'+str(self.x)+','+str(self.y)+'>'
    def __sub__(self,c):
        return Cordinate(self.x-c.x ,self.y-c.y)

    def __eq__(self,c):
        return bool(self.x==c.x and self.y==c.y)


c=Cordinate(3,4)
o=Cordinate(0,0)

print(c.x)


print(Cordinate.distance(c,o))  #mine feel from javaa
#print(c.distance(o))           #mit feel in python


print(c)
print(o)

print(type(c))
print(isinstance(c,Cordinate))


#some methods

print(c-o)
#print(c+o) #you can implement ; def __add__


print(o==c)
#print(c<o) #you can implement ;def __lt__




