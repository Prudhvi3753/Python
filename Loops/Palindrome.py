a=int(input("Enter a number:"))
temp=a
sum=0
while(temp!=0):
    b=temp%10
    sum=sum*10+b
    temp//=10
if(sum==a):
    print(f"The given number {a} is Palindrome")
else:
    print(f"The given number {a} is not Palindrome")