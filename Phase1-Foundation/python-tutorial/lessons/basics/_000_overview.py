#!/usr/bin/env python3
'''
Overview of Python Basics
Day 001 - Lecture 0: Overview
MIS Engineering Journey - Phase 1 Foundation
Learning Source: Jenny's Lectures

This is the first Python script as part of the 12-month MIS Engineering Journey.
Created while following Jenny's Python tutorial on Day 1.

Author: Odili Chinedum Christian
Date: August 19, 2025

'''

import datetime
print("Welcome to Python, Odili!")

# You can print different types of data
print("This is text")           # String (text)
print(42)                       # Number (integer)
print(3.14)                     # Number (decimal/float)
print(True)                     # Boolean (True/False)

# You can print multiple things at once
print("Hello", "Odili", "from", "Voldamort")

# Print with different separators
print("Python", "is", "awesome", sep="-")
print("Learning", "Python", "step", "by", "step", sep=" -> ")

# Special characters in strings
print("This is line 1\nThis is line 2")  # \n creates a new line
print("Tab\tspace\there")                 # \t creates a tab space

print("Hello, MIS Engineering World!")
print("My name is Odili Chinedum Christian")
print("Today I begin my 12-month journey to become a Software Engineer and Data Analyst!")
print("-" * 60)

# Basic arithmetic - calculating my learning journey
days_in_journey = 365
hours_per_week = 15
weeks_in_year = 52
total_learning_hours = (days_in_journey / 7) * hours_per_week

print(f"📅 Journey Duration: {days_in_journey} days")
print(f"⏰ Weekly Commitment: {hours_per_week} hours")
print(f"🎯 Total Learning Hours Planned: {total_learning_hours:.0f} hours")
print(f"📈 That's {total_learning_hours/24:.1f} full days of learning!")

# Personal information display
name = "Odili Chinedum Christian"
current_skill_level = "Complete Beginner"
target_role = "MIS Engineer (Software + Data Analytics)"
motivation_level = 5  # out of 5

print("-" * 60)
print("🚀 PERSONAL PROFILE")
print(f"Name: {name}")
print(f"Current Level: {current_skill_level}")
print(f"Target Role: {target_role}")
print(f"Motivation: {'🔥' * motivation_level} ({motivation_level}/5)")

# Goal breakdown by phase
phases = {
    "Phase 1 (Months 1-3)": "Foundation - Python, Git, Web, SQL",
    "Phase 2 (Months 4-6)": "Core Skills - OOP, Flask, Data Analytics",
    "Phase 3 (Months 7-9)": "Integration - Full-stack, Cloud, ML"
}

print("-" * 60)
print("📋 LEARNING PHASES")
for phase, description in phases.items():
    print(f"{phase}: {description}")

# Commitment statement
print("-" * 60)
print("💪 MY COMMITMENT:")
print("I will code every single day for the next 365 days.")
print("I will build amazing projects that showcase my skills.")
print("I will document my journey and help others learn.")
print("I will become a professional MIS Engineer!")
print("-" * 60)

print("✅ Day 1 Complete - The journey begins!")
print("🎯 Next: Variables, data types, and basic operations")

# Calculate days until target completion
start_date = datetime.date(2025, 8, 19)
end_date = datetime.date(2026, 8, 19)
days_remaining = (end_date - start_date).days

print(f"📅 Days remaining: {days_remaining}")
print("Let's make every day count! 🚀")
