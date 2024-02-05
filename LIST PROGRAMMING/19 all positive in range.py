# Print All Positive Numbers in a Range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
positive_numbers_range = [num for num in range(start_range, end_range + 1) if num > 0]
print("Positive Numbers in the Range:", positive_numbers_range)
