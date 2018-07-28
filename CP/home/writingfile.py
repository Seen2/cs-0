def main():
    f=open('nepy.txt','w')
    f.write('this is new file')
    read()





def read():
    f=open('nepy.txt','r')
    print(f.readlines())

main()
