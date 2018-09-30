

#Class Example

class fraction(object):
    def __init__(self,num,denum):
        self.num=num
        self.denum=denum


    def __str__(self):
        return '<'+str(self.num)+'/'+str(self.denum)+'>'
    def getNum(self):
        return self.num
    def getDnum(self):
        return self.denum


    def add(self,f):
        q=self.denum*f.denum
        p=self.num*f.denum+f.num*self.denum

        return fraction(p,q)   #u can return as __str__

    def sub(self,f):
        q=self.getDnum()*f.getDnum()
        p=self.getNum()*f.getDnum()-f.getNum()*self.getDnum()
        return fraction(p,q)
    def float(self):
        return str(self.num/self.denum)








print('a:',end='')
f=fraction(3,4)
print(f)

print('b:',end='')
o=fraction(1,4)
print(o)

print('a+b:',end='')
print(f.add(o))
print('a-b:',end='')
print(f.sub(o))

print('float view a= {} b={} add={} sub={}'.format(f.float(),o.float(),f.add(o).float(),f.sub(o).float()))
