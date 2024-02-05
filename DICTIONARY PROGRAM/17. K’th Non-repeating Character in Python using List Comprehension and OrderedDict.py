# Example String
my_string = "programming"

# K value
k = 2

# Create a dictionary to store the count of each character
char_count = {}

# Populate the dictionary with character counts
for char in my_string:
    char_count[char] = char_count.get(char, 0) + 1

# Find non-repeating characters
non_repeating_chars = [char for char, count in char_count.items() if count == 1]

# Check if there are enough non-repeating characters to find the K'th one
if len(non_repeating_chars) >= k:
    kth_non_repeating_char = non_repeating_chars[k - 1]
    print("Original String:", my_string)
    print(f"{k}th Non-repeating Character:", kth_non_repeating_char)
else:
    print("There are not enough non-repeating characters to find the K'th one.")
