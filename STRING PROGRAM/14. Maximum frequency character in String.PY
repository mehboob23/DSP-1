from collections import Counter

string = "programming"
char_frequency = Counter(string)
max_frequency_char = max(char_frequency, key=char_frequency.get)
print("Maximum frequency character:", max_frequency_char)
