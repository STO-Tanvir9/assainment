number=int(input("enter a number"))
def even_or_odd(number):
    if number % 2 == 0:
        print("the number ",number,"is even")
    else:
        print("the number",number," is odd")
even_or_odd(number)