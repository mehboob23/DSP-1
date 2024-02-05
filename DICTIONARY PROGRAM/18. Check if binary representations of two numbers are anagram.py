# Example Numbers
num1 = 10
num2 = 5

# Check if binary representations of two numbers are anagram
bin1 = bin(num1)[2:]
bin2 = bin(num2)[2:]
are_anagrams = sorted(bin1) == sorted(bin2)

print("Binary representation of", num1, ":", bin1)
print("Binary representation of", num2, ":", bin2)
print("Are binary representations anagrams:", are_anagrams)
