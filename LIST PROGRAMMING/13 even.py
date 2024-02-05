# Print Even Numbers in a List
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
even_numbers = [num for num in my_list if num % 2 == 0]
print("Even Numbers:", even_numbers)
