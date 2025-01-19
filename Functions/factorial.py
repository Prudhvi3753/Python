def factorial(a):
    fact=1
    if a<0:
        return "Factorial is ni=ot define for negative numbers"
    elif a==0 or a==1:
        return 1
    else:
        for i in range(1,a+1):
            fact*=i
        return fact
a=int(input("Enter a number:"))
res=factorial(a)
print(f"Factorial of {a} is {res}")