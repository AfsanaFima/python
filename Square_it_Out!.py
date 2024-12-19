# Get the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Create a list of square values
squares = []
for num in range(start, end + 1):
    squares.append(num ** 2)

# Separate even and odd squares
even_squares = []
odd_squares = []

for square in squares:
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

# Display the results
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)
