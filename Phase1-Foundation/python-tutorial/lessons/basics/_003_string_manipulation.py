#!/usr/bin/env python3
'''
Day 001 - Lecture 3: String Manipulation - Comprehensive Tutorial
MIS Engineering Journey - Phase 1 Foundation
Learning Source: Jenny's Lectures

This is my third Python script as part of the 12-month MIS Engineering Journey.
Created while following Jenny's Python tutorial on Day 1.

Author: Odili Chinedum Christian
Date: August 19, 2025

'''

print("=== STRING MANIPULATION IN PYTHON ===\n")

# ===== 1. BASIC STRING OPERATIONS =====
print("1. BASIC STRING OPERATIONS")
print("-" * 30)

# String creation
name = "Odili Chinedum Christian"
course = "MIS Engineering"
university = "Universidade Jean Piaget de Angola"

print(f"Name: {name}")
print(f"Course: {course}")
print(f"University: {university}")
print()

# ===== 2. STRING INDEXING AND SLICING =====
print("2. STRING INDEXING AND SLICING")
print("-" * 30)

text = "Python Programming"
print(f"Original text: '{text}'")
print(f"First character: '{text[0]}'")
print(f"Last character: '{text[-1]}'")
print(f"First 6 characters: '{text[0:6]}'")
print(f"Last 11 characters: '{text[7:]}'")
print(f"Every 2nd character: '{text[::2]}'")
print(f"Reversed string: '{text[::-1]}'")
print()

# ===== 3. STRING METHODS - CASE MANIPULATION =====
print("3. CASE MANIPULATION")
print("-" * 30)

sample_text = "mis engineering journey"
print(f"Original: '{sample_text}'")
print(f"Upper: '{sample_text.upper()}'")
print(f"Lower: '{sample_text.lower()}'")
print(f"Title: '{sample_text.title()}'")
print(f"Capitalize: '{sample_text.capitalize()}'")
print(f"Swap case: '{sample_text.swapcase()}'")
print()

# ===== 4. STRING METHODS - SEARCHING AND CHECKING =====
print("4. SEARCHING AND CHECKING")
print("-" * 30)

email = "odili.christian@university.edu.ng"
print(f"Email: '{email}'")
print(f"Contains '@': {email.__contains__('@')}")
print(f"Starts with 'odili': {email.startswith('odili')}")
print(f"Ends with '.ng': {email.endswith('.ng')}")
print(f"Position of '@': {email.find('@')}")
print(f"Position of 'christian': {email.find('christian')}")
print(f"Count of 'i': {email.count('i')}")
print()

# ===== 5. STRING METHODS - CLEANING AND FORMATTING =====
print("5. CLEANING AND FORMATTING")
print("-" * 30)

messy_input = "  Hello World!  \n\t  "
print(f"Original: '{messy_input}'")
print(f"Strip whitespace: '{messy_input.strip()}'")
print(f"Left strip: '{messy_input.lstrip()}'")
print(f"Right strip: '{messy_input.rstrip()}'")

# Replace method
sentence = "I am learning Java programming"
print(f"Original: '{sentence}'")
print(f"Replace Java with Python: '{sentence.replace('Java', 'Python')}'")
print()

# ===== 6. STRING SPLITTING AND JOINING =====
print("6. SPLITTING AND JOINING")
print("-" * 30)

full_name = "Odili Chinedum Christian"
name_parts = full_name.split()
print(f"Full name: '{full_name}'")
print(f"Split into parts: {name_parts}")

csv_data = "Python,JavaScript,SQL,HTML,CSS"
languages = csv_data.split(',')
print(f"CSV data: '{csv_data}'")
print(f"Split languages: {languages}")

# Joining strings
words = ['MIS', 'Engineering', 'Journey', '2025']
joined = ' '.join(words)
print(f"Words list: {words}")
print(f"Joined with spaces: '{joined}'")
print(f"Joined with hyphens: '{'-'.join(words)}'")
print()

# ===== 7. STRING FORMATTING METHODS =====
print("7. STRING FORMATTING METHODS")
print("-" * 30)

name = "Odili"
age = 31
gpa = 3.85

# Method 1: % formatting (old style)
print("Old style: My name is %s, I'm %d years old, GPA: %.2f" % (name, age, gpa))

# Method 2: .format() method
print("Format method: My name is {}, I'm {} years old, GPA: {:.2f}".format(name, age, gpa))
print("Named placeholders: My name is {n}, I'm {a} years old, GPA: {g:.2f}".format(
    n=name, a=age, g=gpa))

# Method 3: f-strings (modern, preferred)
print(f"F-string: My name is {name}, I'm {age} years old, GPA: {gpa:.2f}")
print()

# ===== 8. REAL-WORLD EXAMPLES =====
print("8. REAL-WORLD MIS APPLICATIONS")
print("-" * 30)

# Example 1: Processing user input
user_input = "  ODILI CHINEDUM CHRISTIAN  "
cleaned_name = user_input.strip().title()
print(f"Raw input: '{user_input}'")
print(f"Cleaned: '{cleaned_name}'")

# Example 2: Email validation basics
email = "student@university.edu.ng"
is_valid = "@" in email and "." in email and not email.startswith("@")
print(f"Email: {email}")
print(f"Basic validation: {is_valid}")

# Example 3: Data processing
transaction = "2025-08-19,DEPOSIT,5000.00,ATM_TRANSACTION"
parts = transaction.split(',')
date, type_trans, amount, method = parts
print(f"Transaction: {transaction}")
print(f"Date: {date}, Type: {type_trans}, Amount: ₦{amount}, Method: {method.replace('_', ' ')}")

# Example 4: Report generation
students = ['Odili', 'Chinedu', 'Amaka', 'Kemi']
report_header = "STUDENT ENROLLMENT REPORT"
print(f"\n{report_header.center(40, '=')}")
for i, student in enumerate(students, 1):
    print(f"{i:02d}. {student.upper()}")
print("=" * 40)
print()

# ===== 9. STRING VALIDATION METHODS =====
print("9. STRING VALIDATION")
print("-" * 30)

test_strings = ['123', 'ABC123', 'Hello World', '  spaces  ', 'email@test.com']

for test in test_strings:
    print(f"'{test}' ->", end=" ")
    print(f"Numeric: {test.isdigit()}, ", end="")
    print(f"Alpha: {test.isalpha()}, ", end="")
    print(f"Alphanumeric: {test.isalnum()}, ", end="")
    print(f"Uppercase: {test.isupper()}, ", end="")
    print(f"Lowercase: {test.islower()}")
print()

# ===== 10. ADVANCED TECHNIQUES =====
print("10. ADVANCED TECHNIQUES")
print("-" * 30)

# String multiplication
separator = "-" * 50
print(f"Separator: {separator}")

# Multi-line strings
report = """
STUDENT INFORMATION SYSTEM
==========================
Name: Odili Chinedum Christian
Program: MIS Engineering Journey
Status: Active Learner
Progress: Day 1 of 365
"""
print(report)

# Escape characters
file_path = "C:\\Users\\Odili\\Documents\\MIS-Project\\data.txt"
quote = "She said, \"Learning Python is amazing!\""
print(f"File path: {file_path}")
print(f"Quote: {quote}")

print("\n=== END OF STRING MANIPULATION TUTORIAL ===")
