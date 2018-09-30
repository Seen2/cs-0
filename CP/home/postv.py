def main():
    i=postive()
    print("{} is possetive integer".format(i))

def postive():
    while True:
        print("n is:")
        n=int(input())
        if n>=1:
            break
    return n
if __name__=="__main()__":
    main()
