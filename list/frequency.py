n=int(input("enter a number:"))
l=[]
for _ in range (n):
    e=int(input("enter element:"))
    l.append(e)

f={}

for i in l:
    if i in f:
        f[i]+=1
    else:
        f[i]=1

for i,j in f.items():
    print(i,j)