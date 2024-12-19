# Create a list of squares for numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(f"Squares from 1 to 10: {squares}")

# Filter a list to get even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers from 1 to 20: {evens}")

# Convert a list of strings to uppercase
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
print(f"Uppercase words: {upper_words}")

# Create a list of tuples (number, square) for numbers from 1 to 5
num_square_tuples = [(x, x**2) for x in range(1, 6)]
print(f"Number and their squares from 1 to 5: {num_square_tuples}")

# Flatten a list of lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [item for sublist in list_of_lists for item in sublist]
print(f"Flattened list: {flat_list}")
