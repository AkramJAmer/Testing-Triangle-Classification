# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
    """

    # Input validation: the input values must be between 1 and 200 inclusive
    if a > 200 or b > 200 or c > 200 or a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # Ensure that all inputs are integers
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # Check if the inputs form a valid triangle (sum of any two sides must be greater than the third side)
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # Result variable to reduce return statements
    result = None

    # Check for equilateral triangle
    if a == b == c:
        result = 'Equilateral'
    # Check for right triangle using Pythagoras theorem
    elif (a ** 2 + b ** 2 == c ** 2) or \
         (a ** 2 + c ** 2 == b ** 2) or \
         (b ** 2 + c ** 2 == a ** 2):
        result = 'Right'
    # Check for isosceles triangle (exactly two equal sides)
    elif a == b or b == c or a == c:
        result = 'Isoceles'
    # If no sides are equal, it's a scalene triangle
    else:
        result = 'Scalene'

    return result
