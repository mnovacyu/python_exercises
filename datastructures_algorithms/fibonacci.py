'''
Utilize recursion to create a Fibonacci algorithm.
'''

def fib(n):
    while n >= 1:
        return n + fib(n-1)
    else:
        return 0

print(fib(100))