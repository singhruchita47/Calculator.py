# 1. We define four simple functions for basic math operations
def add(x, y):
    return x + y            # Adds two numbers

def subtract(x, y):
    return x - y            # Subtracts second number from first

def multiply(x, y):
    return x * y            # Multiplies two numbers

def divide(x, y):
    if y == 0:              # Checks if trying to divide by zero to prevent program crash
        return "Error: Division by zero!"
    return x / y            # Divides first number by second

# 2. This is our main application function
def main():
    print("Welcome to the Calculator CLI App!")
    
    while True:             # A loop that keeps running forever until you exit
        # Show the menu
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")
        
        # Take user input for what they want to do
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break           # Stops the 'while True' loop and exits the program
            
        # Check if the user entered a valid choice from 1 to 4
        if choice in ('1', '2', '3', '4'):
            try:
                # Ask for numbers. We use float() to allow decimal numbers (like 2.5)
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                # If they type letters instead of numbers, catch the error and start the loop over
                print("Invalid input. Please enter numeric values.")
                continue
                
            # Check their choice and call the correct function, then print the result
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            # If they enter something like '6' or a letter
            print("Invalid Input. Please enter a valid choice.")

# 3. This tells Python to run the main() function only if this script is executed directly
if __name__ == "__main__":
    main()