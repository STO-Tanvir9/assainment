year=int(input("enter year = "))
def lip_year_ki(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("true")
    else:
        print("false")
lip_year_ki(year)