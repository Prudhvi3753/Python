x=int(input("Enter a number:"))
y=int(input("Enter another number:"))
a=x
b=y
while(b>0):
    r=a%b
    a=b
    b=r
print(f"Gcd of {x} and {y} is {a}")
lcm=(x*y)//a
print(f"lcm is {lcm}")