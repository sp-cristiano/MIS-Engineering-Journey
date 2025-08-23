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

x = int(input("Enter a number: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# The for statements
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
