# Function to find the n'th multiple of a number in Fibonacci Series
def find_nth_multiple_of_number(n, number):
    fib_sequence = [0, 1]
    
    while True:
        current = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(current)
        
        if current % number == 0:
            n -= 1
            if n == 0:
                return current

# Example usage
n_value = int(input("Enter the value of n: "))
number_to_find_multiple = int(input("Enter the number to find multiples in Fibonacci Series: "))

result = find_nth_multiple_of_number(n_value, number_to_find_multiple)

print(f"The {n_value}'th multiple of {number_to_find_multiple} in Fibonacci Series is: {result}")
