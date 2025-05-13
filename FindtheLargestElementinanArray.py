# Largest Element in Array

# Given an array arr[]. The task is to find the largest element and return it.

# Examples:

# Input: arr[] = [1, 8, 7, 56, 90]
# Output: 90
# Explanation: The largest element of the given array is 90.
# Input: arr[] = [5, 5, 5, 5]
# Output: 5
# Explanation: The largest element of the given array is 5.
# Input: arr[] = [10]
# Output: 10
# Explanation: There is only one element which is the largest.
# Constraints:
# 1 <= arr.size()<= 106
# 0 <= arr[i] <= 106

# 1. Brute Force Solution (With Sorting)
# This approach uses sorting to solve the problem. While it might not be the most efficient solution, it still gets the job done.

# Intuition and Approach
# Intuition:

# Sorting the array arranges the elements in ascending order, so the largest element will be at the last position after sorting.

# Approach:

# Sort the Array: Sort the array in non-decreasing order. This makes sure that the largest element is placed at the last index of the array.
# Return the Largest Element: After sorting, the last element in the array is the largest, so return this element.


def largestElement(arr: [], n: int) -> int:
    # Sort the elements first
    arr.sort()

    # Return the largest from the end
    return arr[-1]


# 2. Optimal Solution (Single Pass Solution)
# This approach uses iteration and maintaing the largest number in a variable and returning it.

# Intuition and Approach
# Intuition:

# The idea is to initialize a variable with the first element of the array and then iterate through the array to compare each element with this variable. If any element is larger than the current value, update the variable to this new value. After completing the iteration, the variable will hold the largest element.

# Approach:

# Initialize the Maximum Value: Start by assuming the first element is the largest.
# Iterate Through the Array: Compare each element with the current maximum value. If a larger element is found, update the maximum value.
# Return the Largest Element: After completing the iteration, return the value stored in the maximum variable.

def largestElement(arr: [], n: int) -> int:
    max_num = arr[0]
    
    for num in arr:
        if num > max_num:
            max_num = num
    
    return max_num
