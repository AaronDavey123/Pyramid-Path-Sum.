# Pyramid-Path-Sum.
This script solves a classic problem involving a pyramid-like structure of numbers where you are tasked with finding the maximum path sum from the top of the pyramid to the bottom. Below is a detailed explanation of the code:


## Code Breakdown:

### 1. Imports
```python
import math
import os
import random
import re
import sys
```

### 2. Function Definition (maximum_path)
```python
def maximum_path(node_values):
```

This function is designed to calculate the maximum path sum from the top to the bottom of the pyramid of numbers.

### 3. Calculate Number of Rows:
```python
    node_values_count = 0
    count = 0
    
    while count < len(node_values):
        node_values_count += 1
        count += node_values_count
```
- The idea is to figure out how many rows the pyramid has, based on the total number of elements **(node_values)**.
- In a pyramid structure, the first row has 1 element, the second has 2, the third has 3, and so on.
- The code is incrementing **node_values_count** to figure out how many rows are needed until the total number of elements **(count)** is greater than or equal to the total number of elements in the **node_values** list.

### 4. Constructing the Pyramid:
```python
    pyramid = []
    index = 0
    
    for i in range(node_values_count):
        row = node_values[index:index + i + 1]
        pyramid.append(row)
        index += i + 1
```
- This part constructs the pyramid by slicing the **node_values** list.
- The first row will have 1 element, the second row will have 2 elements, the third will have 3, and so on.
- For example, for **node_values = [1, 2, 3, 4, 5, 6]**, it creates the following pyramid:
```python
[1]
[2, 3]
[4, 5, 6]
```
- ***index*** keeps track of the current position in the ***node_values*** list.


### 5. Dynamic Programming to Calculate Maximum Path:
```python
    for row in range(node_values_count - 2, -1, -1):
        for col in range(row + 1):
            pyramid[row][col] += max(pyramid[row + 1][col], pyramid[row + 1][col + 1])
```
- This is the key part of the algorithm, applying a bottom-up dynamic programming approach to calculate the maximum path sum.
- The loop starts from the second-to-last row **(node_values_count - 2)** and works upwards to the top **(0)**.
- For each cell in the pyramid, it adds the maximum of the two possible paths (down-left or down-right) from the row below.
- For example, if **pyramid[row + 1][col] = 5** and **pyramid[row + 1][col + 1] = 6**, it will add 6 to the current cell in **pyramid[row][col]**.


### 6. Returning the Maximum Path Sum:
```python
    return pyramid[0][0]
```

- After the dynamic programming calculation, the top of the pyramid **(pyramid[0][0])** contains the maximum path sum, which is returned.

## Test Cases
Importing unittest library and function from **max_path** 

```python
import unittest
from max_path import maximum_path

class TestMaximumPath(unittest.TestCase):
```

### Test Case 1: Simple Pyramid with a Clear Path
#### Description: This test case is a basic pyramid where the maximum path sum can be easily traced. The pyramid is as follows:
```python
 def test_simple_pyramid(self):
        node_values = [
            3,
            4, 6,
            5, 7, 8,
            9, 1, 2, 3
        ]
        expected_result = 21  # Corrected expected result (3 -> 6 -> 7 -> 5 = 21)
        actual_result = maximum_path(node_values)
        self.assertEqual(actual_result, expected_result)
```

### Test Case 2: A Pyramid with Only One Row (Edge Case)
#### Description: This test case tests the scenario where the pyramid consists of just one row, meaning there is no path to calculate, and the only value is the sum.
```python
def test_single_row(self):
        node_values = [5]
        expected_result = 5  # Only one value, so it's the path sum.
        actual_result = maximum_path(node_values)
        self.assertEqual(actual_result, expected_result)
```

### Test Case 3: Large Pyramid with Multiple Rows
#### Description: This test case involves a larger pyramid with more rows. The pyramid is as follows:
```python
def test_large_pyramid(self):
        node_values = [
            10,
            2, 5,
            3, 6, 1,
            8, 9, 4, 7
        ]
        expected_result = 30  # Corrected expected result (10 -> 5 -> 6 -> 9 = 30)
        actual_result = maximum_path(node_values)
        self.assertEqual(actual_result, expected_result)
```

### Purpose:
This algorithm is commonly used to solve problems where the goal is to find the optimal path through a triangular or pyramid-like structure, such as the "triangle" problem in algorithmic challenges.






















