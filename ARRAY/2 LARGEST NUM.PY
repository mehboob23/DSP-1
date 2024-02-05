# Function to find the largest element in an array
def find_largest_element(arr):
    if not arr:
        return None  
    else:
        return max(arr)


array = [int(x) for x in input("Enter space-separated elements of the array: ").split()]

largest_element = find_largest_element(array)

if largest_element is not None:
    print(f"The largest element in the array is: {largest_element}")
else:
    print("The array is empty.")