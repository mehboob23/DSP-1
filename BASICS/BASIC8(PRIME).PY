# function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# function to print prime numbers in an interval
def print_primes_in_interval(start, end):
    print(f"Prime numbers in the interval [{start}, {end}]:")
    for number in range(start, end + 1):
        if is_prime(number):
            print(number, end=" ")


start_num = int(input("Enter the start of the interval: "))
end_num = int(input("Enter the end of the interval: "))

if start_num < 0 or end_num < 0 or start_num > end_num:
    print("Invalid interval. Please enter valid start and end values.")
else:
    print_primes_in_interval(start_num, end_num)
