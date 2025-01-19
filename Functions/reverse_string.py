def reverse_string(str1):
    if len(str1)<1:
        return "not possible"
    else:
        return str1[::-1]
str1=input("Enter a string:")
res=reverse_string(str1)
print(f"the reverse of {str1} is {res}")