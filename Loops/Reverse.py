a=int(input("Enter a number:"))
sum=0
while(a!=0):
    b=a%10
    sum=(sum*10)+b
    a//=10
print(f"Reverse of {a} is {sum}")