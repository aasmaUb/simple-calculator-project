# operations.py
# Created by Aasma Ubaid
# Description: Functions for performing basic arithmetic operations


def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract second number from the first."""
    return a - b

def multiply(a, b):
    """multipling two numbers"""
    return a * b

def divide(a, b):
    """It will divide the first number by the second, handling division by Zero"""
    if b == 0:     
        return "Error! Division by Zero"
    else:
        return a / b