s1=int(input("Enter marks of maths:"))
s2=int(input("Enter marks of physics:"))
s3=int(input("Enter marks of chemistry:"))
total=s1+s2+s3
avg=total//3
if(avg>90):
    print("A+")
elif 75<=avg<=90:
    print("A")
elif 50<=avg<=74:
    print("B")
else:
    print("Fail")