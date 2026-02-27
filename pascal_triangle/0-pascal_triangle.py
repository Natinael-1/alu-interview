#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    """
    # Rule: Return an empty list if n <= 0
    if n <= 0:
        return []
    
    # We always start our main triangle list with the first row already inside it
    triangle = [[1]]
    
    # We use a loop to build the rest of the rows, up to 'n'
    for i in range(1, n):
        # 1. Start a new row. It always begins with 1.
        row = [1]
        
        # 2. Look at the row right above the one we are currently building
        previous_row = triangle[i - 1]
        
        # 3. Calculate the middle numbers (if there are any)
        for j in range(1, i):
            sum_of_above = previous_row[j - 1] + previous_row[j]
            row.append(sum_of_above)
        
        # 4. Finish the row. It always ends with 1.
        row.append(1)
        
        # 5. Attach (append) our newly built row to the main triangle
        triangle.append(row)
        
    return triangle
