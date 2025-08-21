#!/usr/bin/env python3
'''
Day 001 - Lecture 7: Control Flow
MIS Engineering Journey - Phase 1 Foundation
Learning Source: Jenny's Lectures and www.w3schools.com

This is my seventh Python script as part of the 12-month MIS Engineering Journey.
Created while following Jenny's Python tutorial and www.w3schools.com on Day 3.

Author: Odili Chinedum Christian
Date: August 19, 2025
'''

# Python conditions and if statement

# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops

# An "if statement" is written by using the if keyword:

a = 33
b = 200

if b > a:
    print("b is greater than a")


# Indentation

# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
# Using indentation indicates a block of code

# You can use any number of spaces, as long as it's consistent within a block of code:

a = 33
b = 200

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")