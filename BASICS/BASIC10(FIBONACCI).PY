#The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

# Function to find the n-th Fibonacci number using recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Function to find the n-th Fibonacci number using iteration
def fibonacci_iterative(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

n = int(input("Enter the value of n to find the n-th Fibonacci number: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
    recursive_result = fibonacci_recursive(n)
    iterative_result = fibonacci_iterative(n)

    print(f"The {n}-th Fibonacci number (recursive): {recursive_result}")
    print(f"The {n}-th Fibonacci number (iterative): {iterative_result}")


