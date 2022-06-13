# Exercise #1
# Create a calculator using functions that asks for two numbers and performs a calculation that the user inputs... Loop until the user chooses not to perform any more calculations.
# Hint: Take yesterday's code from the extra exercise...

def add(a, b):
    print(a+b)
    return a + b


def subtract(a, b):
    print(a-b)
    return a - b


def multiply(a, b):
    print(a*b)
    return a * b


def divide(a, b):
    print(a/b)
    return a / b

done_calculating = 'yes'

while done_calculating == 'yes':

    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    operation = input("Do you want to add, subtract, multiply, or divide: ")

    if operation == 'add':
        add(a, b)

    if operation == 'subtract':
        subtract(a, b)
    
    if operation == 'multiply':
        multiply(a, b)

    if operation == 'divide':
        divide(a, b)

    done_calculating = input("Do you want to perform another calculation? Type 'yes' or 'no': ")



# Exercise 2
# Create a pyramid of X's for n number of levels.

def pyramid(n):
    row = ''
    x_list = 'X'
    while n > 0:
        for num in range(n-1):
            row += 'O'
        row += x_list
        for num in range(n-1):
            row += 'O'
        x_list += 'XX'
        n -= 1
        print(row)
        row = ''
pyramid(3)
