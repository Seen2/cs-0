num=abs(int(input('enter the number:')))
n=[]

while num!=0:
    n.append(num%2)
    num=num//2


print('here is binary of number')

for j in range(1,len(n)+1):
        
    print(n[-j],end='')

print('\ncheck it...')
