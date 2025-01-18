a=int(input("Enter a base number:"))
b=int(input("Enter exponent number:"))
res=1
for i in range(abs(b)):
    res*=a
if b<0:
    res=1/res
print(f"{a} to the Power of {b} is {res}")
