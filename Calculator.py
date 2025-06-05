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
