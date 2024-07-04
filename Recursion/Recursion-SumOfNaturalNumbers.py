def sumOfNaturalNumbers(n):
    if(n == 0):
        return 0
    return n + sumOfNaturalNumbers(n-1)
    
    
print(sumOfNaturalNumbers(5))