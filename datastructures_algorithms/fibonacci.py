'''
Utilize recursion to create a Fibonacci algorithm.
fib(n) will give you the nth number in a Fibonacci sequence

e.g. fib(6) = 8
'''

def fib(n):
    while n >= 3:
        return fib(n-1) + fib(n-2)
    else:
        return 1

print(fib(6))