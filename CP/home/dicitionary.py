grades={'Shweta':'A','Kajal':'A+','Anamika':'A','Saumya':'A','Pragya':'A+++','Satrupa':'A+','Neha':'A','puja':'A+','Nidhi':'A++','Soumya':'A+'}

name=input('Enter name of your Crush:')
print('Gradding of {} crush={}'.format(name,grades[name]))


name=input('Enter name of current crush:')
print('how much grade for this once')
g=input()
grades[name]=g
print('Done with that in our dictionary')

print(grades)

name=input('enter name for crush to search in dictionary:')
print(name in grades)
if name in grades ==True:
    print('hello..Shintu have simillar crush')

else:
    print('Ahaa..you have distinct once..')
    pass

name=input('Enter name of crush to remove from dictionar:')

del(grades[name])
print('Done with that..')

print(grades)
print('here are keys of dictionary grades or list of crush')

print(grades.keys())

print('here is values of dicitionary or grade level of crush')

print(grades.values())




