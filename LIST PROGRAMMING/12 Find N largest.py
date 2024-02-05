# Find N Largest Elements from a List
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
n = int(input("Enter the value of N: "))
n_largest_elements = sorted(my_list, reverse=True)[:n]
print(f"{n} Largest Elements:", n_largest_elements)
