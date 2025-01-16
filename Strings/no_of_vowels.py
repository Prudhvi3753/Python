str=input("Enter a String:")
v=0
str=str.lower()
for i in range (0,len(str)):
    if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u'):
        v=v+1
print("No of Vowels=",v)