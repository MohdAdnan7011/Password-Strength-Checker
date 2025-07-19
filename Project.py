# Password Strenth Checker

import re

# Conditions
# Min 8 chars, digit, upperCase, Lowercase, special Characters

def check_password_strength(password):
    if len(password) <8:
        return "Weak: passwords must be atleast of 8 chars"

    if not any(char.isdigit() for char in password):
        return "Weak:password Must conatin a digit"

    if not any(char.isupper() for char in password):
        return "Weak: password must conatin an upper chars"
    
    if not any(char.islower() for char in password):
        return "weak: password must conatin a lower case"
    
    if not re.search(r'[!@#$%^&*(){}<>.?]', password):
        return "Medium: Password Must Contain a special Characters"    
    
    return "Strong: Your password is secured!"

def passwors_checker():
    print("Welcome To The Password Strength Checker")

    while True:
        password = input("Enter Your Password or (type Exit to quit)")

        if password.lower == "Exit":
            print("Thank You for using This tool")
            break
        result = check_password_strength(password)
        print(result)

# run the Password Checker Tool
if __name__ == "__main__":
    passwors_checker()