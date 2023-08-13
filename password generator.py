import random
import string

def generate_password(length, complexity):
    characters = ""
    
    if "lowercase" in complexity:
        characters += string.ascii_lowercase
    if "uppercase" in complexity:
        characters += string.ascii_uppercase
    if "digits" in complexity:
        characters += string.digits
    if "special" in complexity:
        characters += string.punctuation
    
    if not characters:
        return "Error: No character set selected for password generation."
    
    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

def main():
    print("Password Generator")
    print("------------------")
    
    length = int(input("Enter the desired length of the password: "))
    
    print("Select complexity options:")
    print("1. Lowercase letters")
    print("2. Uppercase letters")
    print("3. Digits")
    print("4. Special characters")
    print("5. Mix all")
    
    complexity_choice = input("Enter your choice (e.g., 1 2 4): ")
    complexity_options = {
        "1": "lowercase",
        "2": "uppercase",
        "3": "digits",
        "4": "special",
        "5": "lowercaseuppercasedigitspecial"
    }
    
    selected_complexities = [complexity_options[choice] for choice in complexity_choice.split()]
    
    generated_password = generate_password(length, selected_complexities)
    
    print("\nGenerated Password:")
    print(generated_password)

if __name__ == "__main__":
    main()
