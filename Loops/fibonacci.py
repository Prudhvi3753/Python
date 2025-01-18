a=int(input("enter a number:"))
b=0
c=1
print(f"{b}\n{c}")
for i in range(1,a):
    temp=b+c
    b=c
    c=temp
    print(temp)
