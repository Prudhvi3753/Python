n=int(input("enter a number:"))
l=[]
for _ in range (n):
    e=int(input("enter element:"))
    l.append(e)
print(l)
sum=0
for i in l:
    sum+=i

print(f"sum of elements in list is {sum}")