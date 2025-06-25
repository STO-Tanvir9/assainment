name=input("enter name")
def palindrome(name):
    if name == name[::-1]:
        print("true")
    else:
        print("false")
palindrome(name)