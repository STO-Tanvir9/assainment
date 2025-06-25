a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
def large(a,b,c):
    if a>b and a>c:
        print("the largest number is A =",a)
    elif b>a and b>c:
        print(b, "is the largest number is B =",b)
    else:
        print(c, "is the largest number is C =",c)
large(a,b,c)