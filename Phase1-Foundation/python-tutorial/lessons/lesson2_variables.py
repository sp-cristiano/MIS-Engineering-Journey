# Lesson 2: Variables and Data Types
# Learn how to store and work with data in Python

# =============================================================================
# VARIABLES - containers that store data values
# =============================================================================

# Creating variables (no need to declare type - Python figures it out!)
name = "Odili Chinedum Christian"     # String (text)
age = 25                              # Integer (whole number)
height = 5.9                          # Float (decimal number)
is_learning_python = True             # Boolean (True/False)
computer_name = "Voldamort"

# Display variables
print("Name:", name)
print("Age:", age)
print("Height:", height, "feet")
print("Learning Python:", is_learning_python)
print("Computer:", computer_name)

print("\n" + "="*50)

# =============================================================================
# DATA TYPES - different kinds of data Python can work with
# =============================================================================

# Numbers
integer_number = 42
float_number = 3.14159
negative_number = -17

print("Integer:", integer_number, "- Type:", type(integer_number))
print("Float:", float_number, "- Type:", type(float_number))
print("Negative:", negative_number, "- Type:", type(negative_number))

print("\n" + "-"*30)

# Strings (text)
first_name = "Odili"
last_name = 'Christian'  # Single or double quotes both work
full_name = first_name + " " + last_name  # String concatenation

print("First name:", first_name)
print("Last name:", last_name)
print("Full name:", full_name)
print("String type:", type(full_name))

print("\n" + "-"*30)

# Booleans (True/False)
is_student = True
is_expert = False
python_is_fun = True

print("Is student:", is_student, "- Type:", type(is_student))
print("Is expert:", is_expert)
print("Python is fun:", python_is_fun)

print("\n" + "="*50)

# =============================================================================
# BASIC OPERATIONS
# =============================================================================

# Math operations
a = 10
b = 3

print("Math with a =", a, "and b =", b)
print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Integer division:", a // b)  # 3 (no decimal)
print("Remainder (modulo):", a % b)  # 1
print("Power:", a ** b)          # 1000 (10 to the power of 3)

print("\n" + "-"*30)

# String operations
greeting = "Hello"
target = "Python learner"
message = greeting + ", " + target + "!"
repeated = "Python! " * 3

print("Concatenation:", message)
print("Repetition:", repeated)
print("Length of message:", len(message))

print("\n" + "-"*30)

# Variable reassignment (variables can change!)
score = 0
print("Initial score:", score)

score = 10
print("After first game:", score)

score = score + 5  # Add to existing value
print("After bonus:", score)

score += 3  # Shorthand for score = score + 3
print("After shorthand addition:", score)

print("\n" + "="*50)

# =============================================================================
# USER INPUT
# =============================================================================

print("Let's get some input from you!")
print("(Note: input() always returns a string)")

# Uncomment these lines to try interactive input:
# user_name = input("What's your name? ")
# print("Nice to meet you,", user_name)

# For now, let's simulate input
user_name = "Odili"  # Simulated input
print("Simulated input - Name:", user_name)

# Converting input to numbers
age_input = "25"  # Simulated input
age_number = int(age_input)  # Convert string to integer
print("Age as string:", age_input, "- Type:", type(age_input))
print("Age as number:", age_number, "- Type:", type(age_number))

print("\n" + "="*50)
print("Lesson 2 complete! You've learned about variables and data types.")
