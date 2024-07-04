# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Function to perform exponentiation
def power(x, y):
    return x ** y

# Display the menu
def menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation")
    print("6. Exit")

# Main function
def main():
    while True:
        menu()

        # Take input from the user
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '6':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")

                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")

                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")

                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")

                elif choice == '5':
                    print(f"{num1} ^ {num2} = {power(num1, num2)}")

            except ValueError:
                print("Invalid input! Please enter numeric values.")

        else:
            print("Invalid input! Please select a valid option.")

if __name__ == "__main__":
    main()
