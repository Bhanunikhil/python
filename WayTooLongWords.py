for i in range(int(input())):
    x=input()
    print(x if len(x)<=10 else x[0] + str(len(x)-2) + x[-1])