from collections import Counter

# Example Strings
str1 = "abc"
str2 = "bcad"

# Python counter and dictionary intersection example
counter1 = Counter(str1)
counter2 = Counter(str2)

intersection_dict = dict(counter1 & counter2)
result_string = ''.join(key * value for key, value in intersection_dict.items())

print("Original Strings:", str1, str2)
print("Result String:", result_string)
