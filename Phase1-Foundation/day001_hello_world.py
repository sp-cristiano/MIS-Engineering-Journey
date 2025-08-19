#!/usr/bin/env python3
"""
My First Python Program - Day 1 of MIS Engineering Journey
Author: voldamort
Date: August 19, 2025
Goal: Start the 12-month transformation from beginner to professional
"""

# My very first Python program!
print("Hello, MIS Engineering World!")
print("My name is voldamort")
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
name = "voldamort"
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
import datetime
start_date = datetime.date(2025, 8, 19)
end_date = datetime.date(2026, 8, 19)
days_remaining = (end_date - start_date).days

print(f"📅 Days remaining: {days_remaining}")
print("Let's make every day count! 🚀")
