#!/usr/bin/env python3
'''
Day 001 - Lecture 5: Basic Operations - Comprehensive Tutorial
MIS Engineering Journey - Phase 1 Foundation
Learning Source: Jenny's Lectures and www.w3schools.com

This is my fifth Python script as part of the 12-month MIS Engineering Journey.
Created while following Jenny's Python tutorial and www.w3schools.com  on Day 1.

Author: Odili Chinedum Christian
Date: August 19, 2025

'''

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
message = f'{greeting}, {target}!' #greeting + ", " + target + "!"
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
