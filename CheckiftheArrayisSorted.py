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

# Time limit: 1 sec


# Optimal Solution
# 1. Problem Statement

# Our goal is to determine whether a given array of integers is sorted in non-decreasing order and then possibly rotated. The function checks whether there is at most one "rotation point" in the array, which would indicate that the array is sorted and rotated.
# Input:
# nums: A list of integers.
# Output:
# True if the array is sorted and rotated; otherwise, False.
# 2. Intuition and Approach
# The problem involves verifying if an array that was originally sorted in non-decreasing order has been rotated. A rotation means that a prefix of the array has been moved to the end. For example, the sorted array [1, 2, 3, 4, 5] could be rotated to become [4, 5, 1, 2, 3].
# The key observation is that in a rotated and sorted array, there should be exactly one place where a "decrease" occurs (i.e., where an element is greater than the next element). This drop signifies the rotation point. If there is more than one such drop, the array is neither sorted nor correctly rotated.

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        rotations = 0
        for i in range(0, len(nums)):
            if nums[i] > nums[(i + 1) % n]:
                rotations += 1
            if rotations > 1:
                return False
        return True