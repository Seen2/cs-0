def printMov(fro,to):
    print('move from '+str(fro)+'to'+str(to))

def Call():
    print('call')



def toh(n,fr,to,sp):
    
    Call()
    if n==1:
        printMov(fr,to)

    

    else:
        toh(n-1,fr,sp,to)
        toh(1,fr,to,sp)
        toh(n-1,sp,to,fr)
    
    




n=int(input('enter the no of disk for Tower:'))
toh(n,1,2,3)



