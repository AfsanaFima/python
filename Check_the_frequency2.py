# Define the test dictionary
test_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 1}

# Value to check the frequency for
value = 1

# Find the frequency of the value in the dictionary
frequency = list(test_dict.values()).count(value)

print(f"Frequency of value {value}: {frequency}")
