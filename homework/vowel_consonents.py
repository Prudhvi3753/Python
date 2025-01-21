s=input("enter a string:")
string=s.lower()
for i in range(0,len(string)):
    if string[i]=="a" or string[i]=="e" or string[i]=="i" or string[i]=="o" or string[i]=="u":
        print(f"{string[i]} is vowel")