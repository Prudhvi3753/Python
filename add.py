"""
name=input()
print("hello",name+"!",sep=",")
"""
#integer input and output
#num=int(input("enter a number:"))
#print("You entered:",num,sep="")

#float input and output
'''num=float(input("enter a float number:"))
print("Value of PI:",num,sep="")
'''

#multiple inputs in a single line
'''
a= input()
x, y, z = a.split(" ")
sum = int(x) + int(y) + int(z)
print(sum)'''

#using sep
#name=input()
#age=int(input())
#print(name,age,sep=",")

#inp=input()
#name,age=inp.split(" ")
#print("name:",name,",age:",age,sep="")

#arithematic operstors
'''x,y=input("enter a and b values:").split(",")
a=int(x)
b=int(y)
print("addition:",a+b,"subtration:",a-b,"multiplication:",a*b,"division:",a/b,"floor division:",a//b)'''

#addition
'''a=int(input("enter a number:"))
b=int(input("enter another number:"))
sum=a+b
print("sum:",sum)'''

#area of circle
'''radius=int(input("enter radius:"))
PI=3.14
area=PI*(radius**2)
print(f"area:{area}")'''

#roots
'''
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=(b**2)-4*a*c
r1=0
r2=0
r1=(-b+(d**(0.5)))/2*a
r2=(-b-(d**(0.5)))/2*a
print("roots:",r1,",",r2,sep="")
'''

#swap numbers using temp
'''a=int(input("enter a number:"))
b=int(input("enter b number:"))
temp=a
a=b
b=temp
print(f"a:{a},b:{b}")'''

#swap without temp
"""a=int(input("enter a number:"))
b=int(input("enter b number:"))
a=a+b
b=a-b
a=a-b
print(f"a={a},b={b}") """

#temperature converter
'''
c=float(input("enter celcius:"))
f=c*(9/5)+32
print(f)
k=273+c
print("kelvin:",k)'''

#currency converter
#a=float(input("enter amount:"))
#USD=0.85
#amount=USD*a
#print(amount)

#if condition
'''w=input()
if w=="sunny":
    print("you can play")
    '''

#if else
'''w=input()
if w=="sunny":
    print("you can play")
else:
    print("you cannot play")
    '''

#if elif else loop

'''w=input("enter weather")
if(w=="sunny"):
    print("you can play cricket")
elif(w=="rainy"):
    print("you can play chess")
else:
    print("you cannot play")
    '''

#example
'''a=5
if(a>5):
    print("greater than 5")'''

#nested loop
'''w=input("enter weather")
t=input("enter time")
if(w=="sunny"):
    if(t=="day"):
        print("you can play")
    elif(t=="night"):
        print("you play inside")
    else:
        print("go to sleep")    
else:
    print("no playing")'''

s='hello world'
print(s[::3])