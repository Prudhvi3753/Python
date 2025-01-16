str1=input("Enter a string:")
str2=input("Enter another string:")
str1=sorted(str1.lower().replace(" ",""))
str2=sorted(str2.lower().replace(" ",""))
if(str1==str2):
    print("anagram")
else:
    print("not anagram")