#! bash usr/bin/env python3
'''
Day 002 - Exercise 2: Personal Information
MIS Engineering Journey - Phase 1 Foundation
Learning Source: Jenny's Lectures

This is the first Python script as part of the 12-month MIS Engineering Journey.
Created while following Jenny's Python tutorial on Day 2.

Author: Odili Chinedum Christian
Date: August 19, 2025

'''

# Personal Information
name = "Odili Chinedum Christian"
age = 25
height = 5.9
is_student = True
is_learning_python = True
depatrtment = "Management Information Systems"
gpa = 4.8

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Student: {is_student}")
print(f"Learning Python: {is_learning_python}")
print(f"Department: {depatrtment}")
print(f"GPA: {gpa}")


# Type checking
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(is_learning_python))
print(type(depatrtment))
print(type(gpa))

# Type conversion

age = str(age)
height = float(height)
is_student = bool(is_student)
is_learning_python = bool(is_learning_python)
gpa = float(gpa)

print(type(age))
print(type(height))
print(type(is_student))
print(type(is_learning_python))
print(type(gpa))


# Boolean Logic

can_graduate = gpa >= 4.5
print(f"Eligible for graduation: {can_graduated}")

