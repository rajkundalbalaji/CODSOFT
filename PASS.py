import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        
        characters = string.ascii_lowercase
    elif complexity == 2:
    
        characters = string.ascii_letters
    elif complexity == 3:
        
        characters = string.ascii_letters + string.digits
    elif complexity == 4:
        
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Complexity level must be between 1 and 4.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        complexity = int(input("Enter complexity level (1-4): "))
        
        if length <= 0:
            print("Password length must be a positive integer.")
            return
        
        password = generate_password(length, complexity)
        print(f"Generated Password: {password}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()