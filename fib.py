n=int(raw_input())

def fib(n):
    counter = 0
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
        
print fib(n)
