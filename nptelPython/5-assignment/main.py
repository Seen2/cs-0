A, AB, B, BC, C, CD, D= 10, 9, 8, 7, 6, 5 , 4

data={}

while(True):
    i=input()
    if (i=='Courses'):

        data['Courses']=[]
        while(True):
            i=input()
            if i=='Students':
                break
            (data['Courses']).append(i)

    if (i=='Students'):
        data['Students']=[]
        while True:
            i=input()
            if (i=='Grades'):
                break
            data['Students'].append(i)

    if i=='Grades' :
        data['Grades']=[]
        while True :
            i=input()
            if i=='EndOfInput' :
                break
            data['Grades'].append(i)

    if i=='EndOfInput' :
        break

output=[]

for student in data['Students']:
    s=student.split('~')
    for grade in data['Grades']:
        g=grade.split('~')
        if g[3]==s[0]:
            if g[4]=='A':
                g[4]=A
            if g[4]=='AB':
                g[4]=AB
            if g[4]=='B':
                g[4]=B
            if g[4]=='BC':
                g[4]=BC
            if g[4]=='C':
                g[4]=C
            if g[4]=='CD':
                g[4]=CD
            if g[4]=='D':
                g[4]=D
            s.append(g[4])
    output.append(s)

outputData=[]

for student in output:
    while len(student)< 2+len(data['Courses']):
        student.append(0)
    avg=0
    for i in range(2,len(student)):
        if student[i]==0:
            student.remove(student[i])
            break
        
        avg=avg+student[i]
    
    avg=avg/(len(student)-2)
    if avg == 0:
      avg=round(avg)
    else:
      avg=round(avg,2)
    avg=str(avg)

    student=student[:2]
    student.append(avg)
    outputData.append(student)



    

outputData.sort()
for student in outputData:
    print("~".join(student))




#input
'''

Courses
TRAN~Transfiguration~1~2011-2012~Minerva McGonagall
CHAR~Charms~1~2011-2012~Filius Flitwick
Students
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Grades
TRAN~1~2011-2012~SLY2301~AB
TRAN~1~2011-2012~SLY2302~B
TRAN~1~2011-2012~SLY2303~B
TRAN~1~2011-2012~SLY2305~A
TRAN~1~2011-2012~SLY2306~BC
TRAN~1~2011-2012~SLY2308~A
TRAN~1~2011-2012~SLY2309~AB
CHAR~1~2011-2012~SLY2301~A
CHAR~1~2011-2012~SLY2302~BC
CHAR~1~2011-2012~SLY2303~B
CHAR~1~2011-2012~SLY2305~BC
CHAR~1~2011-2012~SLY2306~C
CHAR~1~2011-2012~SLY2307~B
CHAR~1~2011-2012~SLY2308~AB
EndOfInput
'''
