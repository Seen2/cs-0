from ExtendedExample0 import *


class UGgurus(gurus):
    def __init__(self,name,year,month,date,yr,proff):
        gurus.__init__(self,name,year,month,date)
        self.y=yr
        self.p=proff

    def work(self):
        print('work as:',end='')
        print(self.p)

    def __str__(self):

        return 'UGgurus:'+str(self.n)+',DOB:'+str(self.d)+',year:'+str(self.y)+' as '+str(self.p)

