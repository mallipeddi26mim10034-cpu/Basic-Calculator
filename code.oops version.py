class Calculator:
    def _init_(self):
        print("Basic Calculator Initialized.")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b


# Main Program
calc = Calculator()

while True:
    print("\n--- Basic Calculator (OOP) ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == "5":
        print("Thank you! Calculator closing...")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Try again.")
        continue

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input! Enter valid numbers.")
        continue

    if choice == "1":
        print("Result =", calc.add(x, y))
    elif choice == "2":
        print("Result =", calc.subtract(x, y))
    elif choice == "3":
        print("Result =", calc.multiply(x, y))
    elif choice == "4":
        print("Result =", calc.divide(x, y))