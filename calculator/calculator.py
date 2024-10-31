import math

print('Select Oparation:\n 1. Add \n 2. Substract \n 3. Multiply \n 4. Divide')

while True:
    choice = input('Enter your choice: (1 / 2 / 3 / 4): ')

    if choice in ('1','2','3','4'):
        try:
            num1 = float(input('Enter your 1st Number: '))
            num2 = float(input('Enter your 2nd Number: '))

            if choice == '1':
                print('Result: ' ,  add(num1 , num2))

            if choice == '2': 
                print('Result: ' , subtract(num1 , num2))

            if choice == '3':
                print('Result: ' , multiply(num1 , num2))

            if choice == '4':
                print('Result: ' , divide(num1 , num2))
        
        except ValueError:
            print('Invalid Input! Please Number Only.')
    else:
        print('Invalid Choice! Please Enter Valid Oparation.')

    next_calculation = input('Do you want to calculate again(y/n): ')

    if next_calculation.lower() != 'y':
        break