#!/usr/bin/python3
"""
This module contains the function pascal_triangle
which generates Pascal's triangle for a given integer n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
        
    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        previous_row = triangle[i - 1]
        
        for j in range(1, i):
            sum_of_above = previous_row[j - 1] + previous_row[j]
            row.append(sum_of_above)
            
        row.append(1)
        triangle.append(row)
        
    return triangle
