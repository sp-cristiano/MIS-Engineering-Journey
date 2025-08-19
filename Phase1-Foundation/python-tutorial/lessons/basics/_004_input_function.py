#!/usr/bin/env python3
'''
Day 001 - Lecture 4: Input Function
MIS Engineering Journey - Phase 1 Foundation
Learning Source: Jenny's Lectures

This is the fourth Python script as part of the 12-month MIS Engineering Journey.
Created while following Jenny's Python tutorial on Day 1.

Author: Odili Chinedum Christian
Date: August 19, 2025

'''


# =============================================================================
# USER INPUT
# =============================================================================

print("Let's get some input from you!")
print("(Note: input() always returns a string)")

# Uncomment these lines to try interactive input:
user_name = input("What's your name? ")
print("Nice to meet you,", user_name)

# Get user input
user_age = input("How old are you? ")
print("You are", user_age, "years old")

# For now, let's simulate input
# user_name = "Odili"  # Simulated input
# print("Simulated input - Name:", user_name)

# Converting input to numbers
age_input = "25"  # Simulated input
age_number = int(age_input)  # Convert string to integer
print("Age as string:", age_input, "- Type:", type(age_input))
print("Age as number:", age_number, "- Type:", type(age_number))

print("\n" + "="*50)
print("Lesson 4 complete! You've learned about input.")
