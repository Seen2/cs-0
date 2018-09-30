class Robot(object):
    i=0
    

    def __init__(self,name='robot',color='none'):
        self.n=name
        self.c=color
        

    def set_id(self,id_no=0):
        self.i=id_no


    def get_id(self):
        print('this is {} with id no.:{}'.format(self.n,self.i))


    def speak(self):
        print('hi i am ',self.n,'with ',self.c,' in mind')

    def __str__(self):

        return 'this is '+str(self.n)+' and i am '+str(self.c)

