# Function to calculate the sum of cubes of first n natural numbers
def sum_of_cubes(n):
    return sum(i**3 for i in range(1, n + 1))

# Example usage
n = int(input("Enter the value of n: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    result = sum_of_cubes(n)
    print(f"The sum of cubes of the first {n} natural numbers is: {result}")
