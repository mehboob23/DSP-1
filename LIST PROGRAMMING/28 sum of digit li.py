# Sum of Number Digits in a List
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
digit_sum_list = [sum(map(int, str(num))) for num in my_list]
print("Sum of Digits in the List:", digit_sum_list)
