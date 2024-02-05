# Print All Negative Numbers in a Range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
negative_numbers_range = [num for num in range(start_range, end_range + 1) if num < 0]
print("Negative Numbers in the Range:", negative_numbers_range)
