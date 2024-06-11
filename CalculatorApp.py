 #he aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division
#Task 1: Create functions for each arithmetic operation.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Task 2: Implement user input to receive numbers and an operation choice.
print("Operation: +, -, *, /")
select = input("Select operations: ")

# System processes numbers based upon the operator the user chose
# add(+) two numbers
if select == "+":
    print(num1, "+", num2, "=", num1+num2)

# subtract(-) two numbers
elif select == "-":
    print(num1, "-", num2, "=", num1-num2)

# multiplies(*) two numbers
elif select == "*":
    print(num1, "*", num2, "=", num1*num2)

# Task 3: Ensure your program can handle division by zero and other potential errors.
elif select == "/":
    print(num1, "/", num2, "=", num1/num2)

else:
    print("Invalid input")