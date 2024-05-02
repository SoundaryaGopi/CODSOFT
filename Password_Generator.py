import random
import string

def generate_password(length):
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Ask user for desired length of password
    length = int(input("Enter the desired length of the password: "))
    
    # Generate password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    # Run the main function
    main()
