def is_prime(a):
    if a<=1:
        return False
    else:
        for i in range(2,(int(a**0.5)+1)):
            if(a%i==0):
                return False
        return True
a=int(input("Enter a number:"))
if is_prime(a):
    print(f"{a} is a prime number")
else:
    print(f"{a} is not prime number")