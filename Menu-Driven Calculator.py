
# Menu-Driven Calculator
# PS No. 25

# Function for Addition
def add(a, b):
    return a + b


# Function for Subtraction
def subtract(a, b):
    return a - b


# Function for Multiplication
def multiply(a, b):
    return a * b


# Function for Division
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


# Function for Power
def power(a, b):
    return a ** b


# Function for Modulus
def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Modulus by zero is not allowed.")
    return a % b


# Function to Display Menu
def show_menu():
    print("\n========== MENU-DRIVEN CALCULATOR ==========")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")
    print("============================================")


# Function to Get Numeric Input
def get_number(message):
    while True:
        try:
            return float(input(message))

        except ValueError:
            print("Invalid number. Enter numeric values only.")


# Main Function
def main():

    while True:

        show_menu()

        try:
            choice = int(input("Enter your choice (1-7): "))

        except ValueError:
            print("Invalid choice. Select 1 to 7.")
            continue

        # Exit Option
        if choice == 7:
            print("Thank you for using the calculator. Exiting...")
            break

        # Validate Menu Choice
        if choice < 1 or choice > 7:
            print("Invalid choice. Select 1 to 7.")
            continue

        # Input Two Numbers
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        try:

            # Addition
            if choice == 1:
                result = add(num1, num2)
                symbol = "+"

            # Subtraction
            elif choice == 2:
                result = subtract(num1, num2)
                symbol = "-"

            # Multiplication
            elif choice == 3:
                result = multiply(num1, num2)
                symbol = "*"

            # Division
            elif choice == 4:
                result = divide(num1, num2)
                symbol = "/"

            # Power
            elif choice == 5:
                result = power(num1, num2)
                symbol = "^"

            # Modulus
            elif choice == 6:
                result = modulus(num1, num2)
                symbol = "%"

            # Display Result
            print(
                f"Result: {num1:g} {symbol} {num2:g} = {result:.2f}"
            )

        except ZeroDivisionError as error:
            print("Error:", error)

        except OverflowError:
            print("Error: The result is too large to calculate.")

        except (ValueError, TypeError):
            print("Error: These values cannot be used for this operation.")


# Program Execution
if __name__ == "__main__":
    main()
