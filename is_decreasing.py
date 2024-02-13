
# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: 2/12/2024
# Description: This file contains a recursive function named is_decreasing that checks if a list of numbers
# is strictly decreasing (each element is less than the preceding one). It returns True if the list is strictly
# decreasing and False otherwise.

def is_decreasing(numbers, index=1):
    # Base case: if we've reached the end of the list, return True
    if index == len(numbers):
        return True
    # If the current element is not less than the previous element, return False
    if numbers[index] >= numbers[index - 1]:
        return False
    # Recursive case: continue to the next element
    return is_decreasing(numbers, index + 1)
