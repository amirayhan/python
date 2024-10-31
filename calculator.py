# oparetor = input('Write the symbol of what you want to do: ')
# num1 = int(input('Enter your 1st Number: '))
# num2 = int(input('Enter your 2nd Number: '))

# if oparetor == '+':
#     result = num1 + num2
#     print(f"Your Result is: {result}")
# elif oparetor == '-':
#     result = num1 - num2
#     print(f"Your Result is: {result}")
# elif oparetor == '*':
#     result = num1 * num2
#     print(f"Your Result is: {result}")
# elif oparetor == '/':
#     result = num1 / num2
#     print(f"Your Result is: {result}")
# elif oparetor == '%':
#     result = num1 % num2
#     print(f"Your Result is: {result}")
# else:
#     print('You wrote wrong')


# Basic Calculator in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    else:
        print("Invalid choice! Please select a valid operation.")
    
    # Ask if the user wants to do another calculation
    next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break
