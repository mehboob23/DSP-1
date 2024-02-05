def reverse_array(arr):
    arr.reverse()


array = [int(x) for x in input("Enter space-separated elements of the array: ").split()]

reverse_array(array)
print(f"The array after reversal is: {array}")