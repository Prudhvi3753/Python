inp=input().split(",")
l=[int(i) for i in inp]
a=int(input("Enter a number:"))
c=0
b=l.count(a)
for i in l:
    if i==a:
        c+=1
print(f"{a} repeats {c} times")
print(b)
