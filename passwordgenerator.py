import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        try:
            password_length = int(input("Enter the desired password length: "))
            if password_length <= 0:
                print("Please enter a valid password length (greater than 0).")
            else:
                password = generate_password(password_length)
                print("Generated Password:", password)
                break
        except ValueError:
            print("Please enter a valid number for password length.")

