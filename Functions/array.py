def array(arr):
    return sorted(arr),max(arr),min(arr)
n=int(input("Enter a number:"))
arr=[]
for i in range(n):
    e=int(input("Enter element"))
    arr.append(e)
sort,maximum,minimum=array(arr)
print(f"sotrted array is {sort} and maximum is {maximum} and minimum is {minimum}")