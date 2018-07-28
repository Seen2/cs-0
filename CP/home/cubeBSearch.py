cube=abs(float(input('enter number:')))
start=0.0
end=cube
i=0
guess=(start + end)/2
while abs(guess**3-cube)>=0.001:
    if guess**3-cube>0.001:
        end=guess

    elif guess**3-cube<0.001:
        start=guess

    guess=(start+end)/2
    i=i+1

print('steps={} and ans={}'.format(i,guess))
