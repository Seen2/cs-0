def main():

   i=int(input("i is:"))
   j=int(input("j is:"))
   swap(i,j)

   print("swaping....\n..swaped")
   print(" i is {}\n j is {}".format(j,i))




def swap(x,y):
    temp=x
    x=y
    y=temp


if __name__=="__main__":
    main()
