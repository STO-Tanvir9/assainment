def sum_of_list(numbers):
    print(sum(numbers))
user = input("Enter numbers separated by spaces: ")
number_list = list(map(int, user.split()))
sum_of_list(number_list)
