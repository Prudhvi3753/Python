a=int(input("enter a number:"))
b=int(input("enter another number:"))
operator=input("enter an operator:").lower()

match operator:
    case 'add':
        print(a+b)
    case 'sub':
        print(a-b)
    case 'div':
        print(a/b) if b!=0 else "error division by zero"
    case 'mul':
        print(a*b)
    case 'mod':
        print(a%b)