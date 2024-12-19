import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits  # All letters and digits
    password = ''.join(random.choice(characters) for _ in range(length))  # Generate password
    return password

# Example usage:
password_length = 8
password = generate_password(password_length)
print(f"Generated password: {password}")
