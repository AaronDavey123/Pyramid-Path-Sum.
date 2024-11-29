#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maximum_path' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY node_values as parameter.
#

def maximum_path(node_values):
    node_values_count = 0
    count = 0
    
    # Calculate how many rows are in the pyramid
    while count < len(node_values):
        node_values_count += 1
        count += node_values_count
        
    pyramid = []
    index = 0
    
    # Build the pyramid structure by slicing node_values into rows
    for i in range(node_values_count):
        row = node_values[index:index + i + 1]  # Each row has increasing elements
        pyramid.append(row)
        index += i + 1

    # Debug: Check pyramid construction
    print("Pyramid Structure:")
    for row in pyramid:
        print(row)

    # Perform bottom-up dynamic programming to find the maximum path sum
    for row in range(node_values_count - 2, -1, -1):  # Start from second last row
        for col in range(row + 1):  # Traverse each element in the row
            # Add the maximum of the two adjacent elements from the row below
            pyramid[row][col] += max(pyramid[row + 1][col], pyramid[row + 1][col + 1])

            # Debug: Track changes in each cell during the DP process
            print(f"Row {row}, Col {col}: Updated value = {pyramid[row][col]}")
    
    # The top element will now contain the maximum path sum
    return pyramid[0][0]





