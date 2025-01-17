a=int(input("enter a number:"))
c=0
while(a!=0):
    b=a%10
    c+=1
    a//=10
print(f"No Of Digits in {a} is {c}")