import random
import string

print("🔐 Welcome to the Password Generator!")
print("You can create strong passwords with letters, numbers, and symbols.\n")

length = input("Enter the desired password length (e.g., 8, 10, 12): ")

if length.isdigit():
    length = int(length)
    
    print("Choose password strength level:")
    print("1 ➜ Letters only")
    print("2 ➜ Letters and Numbers")
    print("3 ➜ Letters, Numbers, and Symbols")
    level = input("Enter 1, 2, or 3: ")

    if level == "1":
        characters = string.ascii_letters
    elif level == "2":
        characters = string.ascii_letters + string.digits
    elif level == "3":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("❌ Invalid strength level selected.")
        characters = ""

    if characters:
        password = ""
        for i in range(length):
            password += random.choice(characters)

        print("\n✅ Your generated password is:\n", password)
        print("Tip: Copy and save it in a safe place.")
else:
    print("❌ Please enter a valid number for password length.")

#Output Display:

# 🔐 Welcome to the Password Generator!
# You can create strong passwords with letters, numbers, and symbols.

# Enter the desired password length (e.g., 8, 10, 12): 8
# Choose password strength level:
# 1 ➜ Letters only
# 2 ➜ Letters and Numbers
# 3 ➜ Letters, Numbers, and Symbols
# Enter 1, 2, or 3: 3

# ✅ Your generated password is:
#  !6,y9ojx
# Tip: Copy and save it in a safe place.