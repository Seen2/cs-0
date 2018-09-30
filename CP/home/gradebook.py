class grades(object):


    def __init__(self):
        self.grade={}


    def addStudent(self,student='empty',grade='Nan'):
        self.grade[student]=grade

    def addGrade(self,student='empty',grade='Nan'):

            self.grade[student]=grade

    def removeStudent(self,student):
        del(self.grade[student])


    def __str__(self):
        a=list(self.grade.keys())
        b=list(self.grade.values())

        for i in range(len(a)):
           
        

            print((a[i]) +' is student have grade:'+(b[i]))
        return ''
        
