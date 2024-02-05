def count_matching_characters(str1, str2):
    return sum(1 for char1, char2 in zip(str1, str2) if char1 == char2)

string1 = "hello"
string2 = "hola"
matching_count = count_matching_characters(string1, string2)
print("Number of matching characters:", matching_count)
