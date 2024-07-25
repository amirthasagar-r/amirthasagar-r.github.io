import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        # Ask the32 user for the desired length of the password
        length = int(input("Enter the length of the password: "))
        
        if length <= 0:
            print("Password length should be greater than zero.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print("Generated Password:", password)
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
