a=int(input("enter a number:"))
temp=a
sum=0
while(temp!=0):
    b=temp%10
    sum+=b*b*b
    temp//=10
if(sum==a):
    print("Armstrong number")
else:
    print("Not Armstrong number")