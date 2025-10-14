# 7. Recursion – Fibonacci Series

n = int(input("Enter a length : "))

def func(n):
    if n==0 or n==1:
        return n
    else:
        return func(n-1) + func(n-2)
    
for i in range(n):
    print(func(i))