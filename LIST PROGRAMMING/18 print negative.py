# Print Negative Numbers in a List
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
negative_numbers = [num for num in my_list if num < 0]
print("Negative Numbers:", negative_numbers)
