def interchange_first_and_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]

# Example usage
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]

interchange_first_and_last(my_list)
print(f"The list after interchanging first and last elements is: {my_list}")