n=int(input("enter a number:"))
l=[]
for _ in range (n):
    e=int(input("enter element:"))
    l.append(e)
    
'''l.sort()
print("maximum:",l[-1])
print("minimum:",l[0])'''

maxi,mini=l[0],l[0]
for i in l:
    if maxi<i:
        maxi=i
    elif mini>i:
        mini=i
print(maxi,mini)