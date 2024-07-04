def printNTo1(n):
    if(n==0):
        return 0
    print(n)
    return printNTo1(n-1)

printNTo1(30)