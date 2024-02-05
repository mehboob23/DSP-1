def find_remainder_of_array_multiplication(arr, n):
    result = 1
    
    # Calculate the product of array elements
    for num in arr:
        result = (result * num) % n
    
    return result

# Example usage
array = [int(x) for x in input("Enter space-separated elements of the array: ").split()]
divisor = int(input("Enter the value of n: "))

remainder = find_remainder_of_array_multiplication(array, divisor)
print(f"The remainder of the array multiplication divided by {divisor} is: {remainder}")
