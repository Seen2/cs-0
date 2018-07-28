

# function calls

def main():
    cough(3)
    achho(3)
    happ(3)

def cough(n):
    say("cough",n)


def achho(n):
    say("achho",n)


def happ(n):
    say("happ",n)


def say(word,n):
    for i in range(n):
        print("{}".format(word))



if __name__=="__main__":
    main()
