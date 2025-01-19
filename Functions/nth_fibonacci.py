def nth_fib(n):
    a,b=0,1
    if n<1:
        return "not possible for negative numbers"
    else:
        for _ in range(n-1):
            a,b=b,a+b
            n-=1
        return a
n=int(input("enter a number:"))
res=nth_fib(n)
print(f"{n}th fibonacci is {res}")