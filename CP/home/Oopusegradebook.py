from gradebook import *

book=grades()

book.addStudent('Shintu')
print(book)


book.addGrade('Shintu','A')
print(book)

print('After Mark')
book.addStudent('Mark')
print(book,end='')

book.addGrade('Mark','A+++')

print(book)




book.removeStudent('Shintu')
print('after removing')

print(book)

