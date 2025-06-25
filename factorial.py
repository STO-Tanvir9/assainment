number=int(input("enter a number"))
def factorial(number):
    if number <= 0:
        print("Factorial is not defined for negative numbers.")
    elif  number==0 or number == 1:
        print(1)
    else:
        result=1
        for i in range(2, number + 1):
            result *= i
        print(result)
factorial(number)