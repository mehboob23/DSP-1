# Using the 'in' keyword
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]

element_to_check = int(input("Enter the element to check: "))

if element_to_check in my_list:
    print(f"{element_to_check} is present in the list.")
else:
    print(f"{element_to_check} is not present in the list.")