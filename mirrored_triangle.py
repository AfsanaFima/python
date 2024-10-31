def combined_triangles(n):
    for i in range(1, n + 1):
        # Mirrored right-angled triangle
        print(' ' * (n - i) + '*' * i, end='')
        # Right-angled triangle
        print('*' * i)

# Example usage
n = int(input("Enter the number of rows: "))
combined_triangles(n)
