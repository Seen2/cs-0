import sys



if len(sys.argv)==2:
    print("hello,{}".format(sys.argv[1]))



else:
    print("hello, world")



if len(sys.argv)>2:
    for i in range(len(sys.argv)):
        print(sys.argv[i])

else:
    pass
