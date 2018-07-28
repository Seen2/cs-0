#taking input what i want

while True:
    try:
        n=int(input('enter an integer:'))
        print('ahha..i get integer..')
        break
    except ValueError:
        print('you entered wrong value..try again..')



print('entered integer is:',n)

#let me work with files

'''if all statements under try get executed counter jump out of except
if a single statement cause error it goes to exception part
'''
try:
    filename=input('enter file to read:')
    f=open(filename,'r')
    print('file opening success')
except IOError:
    print('error with name..')
    

except:
    print('something very bad')

else:
    for line in f:
        print(line)

finally:
    f.close()



