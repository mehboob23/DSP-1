# Print All Odd Numbers in a Range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
odd_numbers_range = [num for num in range(start_range, end_range + 1) if num % 2 != 0]
print("Odd Numbers in the Range:", odd_numbers_range)
