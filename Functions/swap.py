x=int(input("Enter a number:"))
y=int(input("Enter another number:"))
def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b
x,y=swap(x,y)
print(x,y,sep=" ")