# Problem statement
# You have been given an array ‘a’ of ‘n’ unique non-negative integers.



# Find the second largest and second smallest element from the array.



# Return the two elements (second largest and second smallest) as another array of size 2.



# Example :
# Input: ‘n’ = 5, ‘a’ = [1, 2, 3, 4, 5]
# Output: [4, 2]

# The second largest element after 5 is 4, and the second smallest element after 1 is 2.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# 4
# 3 4 5 2
# Sample Output 1 :
# 4 3
# Explanation For Sample Input 1 :
# The second largest element after 5 is 4 only, and the second smallest element after 2 is 3.
# Sample Input 2 :
# 5
# 4 5 3 6 7
# Sample Output 2 :
# 6 4
# Expected Time Complexity:
# O(n), Where ‘n’ is the size of an input array ‘a’.
# Constraints:
# 2 ≤ 'n' ≤ 10^5
# 0 ≤ 'a'[i] ≤ 10^9

# Brute Force Solution
# 1. Problem Statement
# Objective: Our task is to find the second smallest and second-largest elements in an array, assuming there are no duplicate elements in the array.
# Expected Input and Output:
# Input: An integer n representing the size of the array, and an array a of integers.
# Output: A list containing two integers: [second_largest, second_smallest].
# 2. Intuition and Approach
# Intuition:
# By sorting the array, we can easily access the second smallest and second-largest elements by their positions in the sorted array. Since the array is sorted, the smallest element will be at the first index, and the largest element will be at the last index. Consequently, the second smallest will be at index 1, and the second largest will be at index -2 (second to last).
# Approach:
# Sort the Array: Sorting the array will arrange the elements in ascending order.
# Access the Second Smallest and Second Largest:
# The second smallest element will be at index 1.
# The second-largest element will be at index -2.
# Return the Result: Return the elements as a list [second_largest, second_smallest].

def getSecondOrderElements(n: int, a: List[int]) -> List[int]:
    # Sort the array
    a.sort()

    # Second minimum will be on 1st index
    # Second largest will be on last second index
    return [a[-2], a[1]]

# Better Solution (Two Pass Solution)
# 1. Problem Statement
# Objective: Our goal is to find the second smallest and second largest elements in an array without sorting the array. The solution should assume that the array has no duplicate elements.
# Expected Input and Output:
# Input: An integer n representing the size of the array, and an array a of integers.
# Output: A list containing two integers: [second_largest, second_smallest].
# 2. Intuition and Approach
# Intuition:
# The problem can be solved by iterating through the array twice:
# First Pass: Identify the smallest and largest elements in the array.
# Second Pass: Identify the second smallest and second-largest elements by excluding the smallest and largest elements found in the first pass.
# Approach:
# Initialize Variables: Start by initializing variables small, second_small, large, and second_large to hold the smallest, second smallest, largest, and second-largest values. These are initialized to positive and negative infinity, respectively.
# First Iteration: Iterate through the array to find the smallest and largest elements.
# Second Iteration: Iterate through the array again to find the second smallest and second-largest elements, ensuring these are not the same as the smallest and largest elements found earlier.
# Return the Result: Return the second-largest and second-smallest elements as a list.

def getSecondOrderElements(n: int, a: List[int]) -> List[int]:
    # Initialize variables to track smallest, second smallest, largest, and second largest elements
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")

    # Step 1: Find the smallest and largest number in the array
    for i in range(0, len(a)):
        small = min(small, a[i])  # Update smallest element if current element is smaller
        large = max(large, a[i])  # Update largest element if current element is larger

    # Step 2: Find the second smallest and second largest
    for i in range(0, len(a)):
        if a[i] < second_small and a[i] != small:
            second_small = a[i]  # Update second smallest if current element is smaller but not the smallest
        if a[i] > second_large and a[i] != large:
            second_large = a[i]  # Update second largest if current element is larger but not the largest

    # Step 3: Return the result as a list
    return [second_large, second_small]

# Optimal Solution (Single Pass Solution)
# 1. Problem Statement
# Our goal is to find the second smallest and the second largest elements in a list of integers. The function receives two inputs: an integer n representing the number of elements in the list, and a list a of integers. The output of the function is a list containing two elements: the second largest and the second smallest elements from the input list.
# Input:
# n: The number of elements in the list a.
# a: A list of integers.
# Output: A list containing two integers:
# The first integer is the second largest element in a.
# The second integer is the second smallest element in a.
# 2. Intuition and Approach
# The problem is approached by iterating through the list and maintaining four variables:
# small: To track the smallest element found so far.
# second_small: To track the second smallest element.
# large: To track the largest element.
# second_large: To track the second largest element.
# As the function iterates over the list:
# It updates the small and second_small whenever a smaller or second smallest element is encountered.
# Similarly, it updates the large and second_large whenever a larger or second largest element is encountered.
# By the end of the loop, the function has identified both the second smallest and second largest elements, which are returned as a list.

def getSecondOrderElements(n: int, a: List[int]) -> List[int]:
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")

    for i in range(0, len(a)):
        if a[i] < small:
            second_small = small
            small = a[i]
        elif a[i] < second_small and a[i] != small:
            second_small = a[i]
        if a[i] > large:
            second_large = large
            large = a[i]
        elif a[i] > second_large and a[i] != large:
            second_large = a[i]

    return [second_large, second_small]

