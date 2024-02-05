import random
import string

target_string = "python"
generated_string = ""

while generated_string != target_string:
    generated_string = ''.join(random.choices(string.ascii_lowercase, k=len(target_string)))

print("Generated String:", generated_string)
