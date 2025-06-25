number=int(input("enter a nuber = "))
def prime(number):
    if number <= 1:
        print("false")
    else:
        if number % 2 == 0:
            print("false")
        else:
            print("true")
prime(number)
