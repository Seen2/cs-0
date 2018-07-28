from array import array
array=[]
j=0

for i in range(4):
    array[j]=int (input("enter:"))
    j=j+1


j=0
for i in range(4):
     print("\t{}".format(array[j]))
     j=j+1

