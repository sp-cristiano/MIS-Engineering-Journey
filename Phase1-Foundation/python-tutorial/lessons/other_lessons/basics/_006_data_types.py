#!/usr/bin/env python3
'''
Day 001 - Lecture 6: Data Types
MIS Engineering Journey - Phase 1 Foundation
Learning Source: Jenny's Lectures and www.w3schools.com

This is my sixth Python script as part of the 12-month MIS Engineering Journey.
Created while following Jenny's Python tutorial and www.w3schools.com on Day 6.

Author: Odili Chinedum Christian
Date: August 19, 2025
'''


# =============================================================================
# DATA TYPES - different kinds of data Python can work with
# =============================================================================

'''
Built-in Data Types

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	NoneType
'''

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
