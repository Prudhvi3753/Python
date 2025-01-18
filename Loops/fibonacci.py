'''a=int(input("enter a number:"))
b=0
c=1
print(f"{b}\n{c}")
for i in range(1,a):
    temp=b+c
    b=c
    c=temp
    print(temp)'''

n=int(input("Enter a number:"))
a,b=0,1
while(a<=n):
    print(a,end=" ")
    a,b=b,a+b

