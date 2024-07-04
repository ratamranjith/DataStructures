def fibo(n):
    if(n <= 1):
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def fibonacci(n):
    for i in range(n):
        if(i < n):
            print(fibo(i))

fibonacci(10)