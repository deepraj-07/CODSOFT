print("🔢 Welcome to the Multi-Feature Calculator!")
print("You can perform: +(Addition), -(Subtraction), *(MUltiplication), /(Division), %(Modulus), ^ (power), // (floor division)")
print("Type 'exit' at any point to stop the calculator.\n")

history = []

while True:
    num1 = input("Enter the first number: ")
    if num1 == "exit":
        break

    num2 = input("Enter the second number: ")
    if num2 == "exit":
        break

    if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
        num1 = float(num1)
        num2 = float(num2)
    else:
        print("❗ Invalid input. Please enter valid numbers.\n")
        continue

    print("Choose an operation to perform:")
    print(" + > Addition")
    print(" - > Subtraction")
    print(" * > Multiplication")
    print(" / > Division")
    print(" % > Modulus")
    print(" ^ > Power (Exponential)")
    print(" // > Floor Division")

    opr = input("Enter your chosen operation: ")

    if opr == "exit":
        break

    if opr == "+":
        result = num1 + num2
    elif opr == "-":
        result = num1 - num2
    elif opr == "*":
        result = num1 * num2
    elif opr == "/":
        if num2 == 0:
            result = "❌ Error: Cannot divide by zero."
        else:
            result = num1 / num2
    elif opr == "%":
        if num2 == 0:
            result = "❌ Error: Cannot perform modulus by zero."
        else:
            result = num1 % num2
    elif opr == "^":
        result = num1 ** num2
    elif opr == "//":
        if num2 == 0:
            result = "❌ Error: Cannot perform floor division by zero."
        else:
            result = num1 // num2
    else:
        result = "⚠️ Invalid operation. Please choose a correct one from the list."

    print("✅ Result:", result)
    history.append(str(num1) + " " + opr + " " + str(num2) + " = " + str(result))
    print()

    show = input("Would you like to see the calculation history? (yes/no): ")
    if show == "yes":
        print("\n🧾 Previous Calculations:")
        for item in history:
            print(" ", item)
        print()

#Output Display: 

# 🔢 Welcome to the Multi-Feature Calculator!
# You can perform: +(Addition), -(Subtraction), *(MUltiplication), /(Division), %(Modulus), ^ (power), // (floor division)
# Type 'exit' at any point to stop the calculator.

# Enter the first number: 25
# Enter the second number: 25
# Choose an operation to perform:
#  + > Addition
#  - > Subtraction
#  * > Multiplication
#  / > Division
#  % > Modulus
#  ^ > Power (Exponential)
#  // > Floor Division
# Enter your chosen operation: *
# ✅ Result: 625.0

# Would you like to see the calculation history? (yes/no): yes

# 🧾 Previous Calculations:
#   25.0 * 25.0 = 625.0

# Enter the first number: 20
# Enter the second number: 30
# Choose an operation to perform:
#  + > Addition
#  - > Subtraction
#  * > Multiplication
#  / > Division
#  % > Modulus
#  ^ > Power (Exponential)
#  // > Floor Division
# Enter your chosen operation: +
# ✅ Result: 50.0

# Would you like to see the calculation history? (yes/no): yes

# 🧾 Previous Calculations:
#   25.0 * 25.0 = 625.0
#   20.0 + 30.0 = 50.0

# Enter the first number: 30
# Enter the second number: 5
# Choose an operation to perform:
#  + > Addition
#  - > Subtraction
#  * > Multiplication
#  / > Division
#  % > Modulus
#  ^ > Power (Exponential)
#  // > Floor Division
# Enter your chosen operation: /
# ✅ Result: 6.0

# Would you like to see the calculation history? (yes/no): Yes
# Enter the first number: 20
# Enter the second number: 4
# Choose an operation to perform:
#  + > Addition
#  - > Subtraction
#  * > Multiplication
#  / > Division
#  % > Modulus
#  ^ > Power (Exponential)
#  // > Floor Division
# Enter your chosen operation: %
# ✅ Result: 0.0