





#multiple return

def f(prmtr1,prmtr2):
    print('here function and para1={}\npara2={}'.format(prmtr1,prmtr2))
    return (prmtr1+prmtr2)
print('enter something twice')
p1=input()
p2=input()

print(''+f(p1,p2))



def shed(inst,period,sub):
    print('inst={},period={},subject={}'.format(inst,period,sub))
    s=('for '+sub+'instructor is '+inst+'in period '+period)
    return s;
print(shed('David','1st','CS50'))

