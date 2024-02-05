from collections import Counter

# Example List
my_list = [1, 2, 2, 3, 3, 3]

# Python dictionary, set, and counter to check if frequencies can become the same
counter_dict = Counter(my_list)
frequency_set = set(counter_dict.values())
can_become_same = len(frequency_set) == 1

print("Original List:", my_list)
print("Can frequencies become the same:", can_become_same)
