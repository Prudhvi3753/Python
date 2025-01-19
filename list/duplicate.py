n=int(input("enter a number:"))
l=[]
for _ in range (n):
    e=int(input("enter element:"))
    l.append(e)

'''a=set(l)
b=list(a)
print(f"{a}\n{b}")'''

l1=[]
for item in l:
    if item in l1:
        continue
    else:
        l1.append(item)
print(l1)