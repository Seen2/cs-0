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



    

