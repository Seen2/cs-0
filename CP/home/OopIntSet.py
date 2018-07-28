class setInt(object):
        
    def __init__(self):
         self.l=[]   #creating list as object


    def insert(self,o):

        try:
            self.o=o
            if o not in self.l:
                self.l.append(o)

        except:
            raise ValueError ('some thing wrong attempt..')

    def remove(self,o):
        try:
            self.o=o
            self.l.remove(o)

        except:
            raise ValueError('wrong attemt..')

    def search(self,o):
        self.o=o
        if o in self.l:
            return True
        else:
            return False

    def __str__(self):
        return str(self.l)


sets=setInt()
print(sets)


sets.insert(2)
print(sets)
sets.insert(3)
sets.insert(4)

print(sets)

sets.remove(3)
print(sets)


sets.insert(6)
sets.insert(9)

print(sets)


print(sets.search(9))
print(sets.search(4))
print(sets.search(19))

