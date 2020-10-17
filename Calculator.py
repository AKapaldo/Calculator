"""
Author: Andrew Kapaldo
Date: October 11, 2020
Version 1.0
Python 3.8
"""

# Set Variables
valid = False
numValid = False
calculation = ""
operation = ""
num1 = ""
num2 = ""
sign = ""
test = ""

# Take inputs and verify they are valid
while not valid or not numValid:
    num1 = input("Enter Number: ")
    sign = input("Enter +, -, /, or *: ")
    num2 = input("Enter Second Number: ")
    try:
        test = float(num1), float(num2)
        if test:
            num1 = float(num1)
            num2 = float(num2)
            numValid = True
        else:
            valid = False
            numValid = False
    except ValueError:
        print("Invalid input. Try again. You must enter numbers.")

# Do some math
    operation = str(num1) + " " + sign + " " + str(num2) + " ="
    if sign == "+":
        calculation = num1 + num2
        valid = True
    elif sign == "-":
        calculation = num1 - num2
        valid = True
    elif sign == "/":
        try:
            calculation = num1 / num2
            valid = True
        except ZeroDivisionError:
            valid = False
            numValid = False
            print("You can not divide by 0. Try Again.")
    elif sign == "*":
        calculation = num1 * num2
        valid = True
    else:
        valid = False
        numValid = False
        print("Invalid input. Try again. You must enter +, -, *, or /")

# Create Graphical Calculator Output
line1 = "---------------------\n"
line2 = f"{'| ' + str(operation)  :<19} |\n"
line3 = f"{'|'} {str(calculation) + '|' :>19}\n"
line4 = f"{'| '  :<19} |\n"
line5 = "|\tAC\tC\t \t/\t|\n"
line6 = "|\t7\t8\t9\t*\t|\n"
line7 = "|\t4\t5\t6\t-\t|\n"
line8 = "|\t1\t2\t3\t+\t|\n"
line9 = "|\t0\t \t.\t=\t|\n"
line10 = "---------------------\n"
calcPict = line1 + line2 + line3 + line1 + line4 + line5 + line6 + line7 + line8 + line9 + line10

# Print output
print(calcPict)
print(operation, calculation)
