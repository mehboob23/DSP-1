def swap_elements(lst, index1, index2):
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        lst[index1], lst[index2] = lst[index2], lst[index1]

# Example usage
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]

index_to_swap1 = int(input("Enter the index of the first element to swap: "))
index_to_swap2 = int(input("Enter the index of the second element to swap: "))

swap_elements(my_list, index_to_swap1, index_to_swap2)
print(f"The list after swapping elements at indices {index_to_swap1} and {index_to_swap2} is: {my_list}")