from collections import Counter

string = "programming"
char_frequency = Counter(string)
least_frequent_char = min(char_frequency, key=char_frequency.get)
print("Least frequent character:", least_frequent_char)
