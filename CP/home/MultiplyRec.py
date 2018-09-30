


#recursion multiply

def mult(a,b,s):
    
    if(b==1):
        
        return s
    else:
        s=s+a

        return mult(a,b-1,s)



a=int(input('enter a:'))
b=int(input('enter b:'))
print(mult(a,b,a))
