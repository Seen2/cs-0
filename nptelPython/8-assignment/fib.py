def main():

    n=int(input('enter the number:'))
    fibTable=[0]
    for i in range(1,n+1):
        if i<=2:
            f=1
        else:
            f=fibTable[i-1]+fibTable[i-2]
        fibTable.append(f)
        print(fibTable[i])

if __name__=="__main__":
    main()
