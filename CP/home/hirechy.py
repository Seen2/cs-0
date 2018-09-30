class animal(object):
    def __init__(self,name,age):
        self.n=name
        self.a=age

    def get_name(self):
        return self.n
    def get_age(self):
        return self.a
    def set_name(self,name):
        self.n=name

    def set_age(self,age):
        self.a=age

    def __str__(self):
        return 'name='+str(self.n)+', age='+str(self.a)

class cat(animal):

    def speak(self):
        print('meow...')

    def __str__(self):
        return 'cat:'+str(self.n)+' age:'+str(self.a)


class person(animal):


    def eat(self):
        print('all three..')

    def __str__(self):

        return 'person:'+str(self.n)+' age='+str(self.a)


class stud(person):


    def __init__(self,name,age,proff):
        self.n=name
        self.a=age
        self.p=proff

    def eat(self):
        print('i love murga bhhat...BC')

    def study(self):
        print('still in python moode..')

    def __str__(self):
        return 'student:'+str(self.n)+' age:'+str(self.a)+'is a '+str(self.p)


