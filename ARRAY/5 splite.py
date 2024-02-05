def split_and_add_to_end(arr, split_index):
    if 0 <= split_index < len(arr):
        arr[:] = arr[split_index:] + arr[:split_index]

array = [int(x) for x in input("Enter space-separated elements of the array: ").split()]
split_position = int(input("Enter the index to split the array: "))

split_and_add_to_end(array, split_position)
print(f"The array after splitting and adding to the end is: {array}")