import datetime
class person:

    pid=1

    def __init__(self,name,year,month,date):
        self.n=name
        self.d=datetime.date(year,month,date)

        self.tag=person.pid
        

    def age(self):


        return (datetime.date.today()-self.d)


    def __str__(self):
        return 'name:'+str(self.n)+' dob:'+str(self.d)


class gurus(person):
    gid=1

    def __init__(self,name,year,month,date):
        self.n=name
        self.d=datetime.date(year,month,date)
        self.tag=gurus.gid
        gurus.gid +=1

    def age(self):


        return (datetime.date.today()-self.d)

    def __lt__(self,o):
        if(self.tag<o.tag):
            return True
        else:

            return False

    def __str__(self):
        return 'name:'+str(self.n)+' dob:'+str(self.d)


