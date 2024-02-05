# Function to find the largest element in an array
def find_largest_element(arr):
    if not arr:
        return None  # Return None for an empty array
    else:
        return max(arr)

# Example usage
array = [int(x) for x in input("Enter space-separated elements of the array: ").split()]

largest_element = find_largest_element(array)

if largest_element is not None:
    print(f"The largest element in the array is: {largest_element}")
else:
    print("The array is empty.")