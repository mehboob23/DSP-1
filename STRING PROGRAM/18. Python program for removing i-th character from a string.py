def remove_ith_character(s, i):
    return s[:i] + s[i+1:]

string = "Python"
i = 2
result = remove_ith_character(string, i)
print(f"After removing {i}th character:", result)
