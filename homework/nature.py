number=int(input("Enter a number:"))
if number>0 and number%2==0:
    print("Positive and even number")
elif number>0 and number%2!=0:
    print("Positive and odd")
elif number<0 and number%3==0:
    print("Negative and Divisible by 3")
elif number==0:
    print("Zero")