# Example 1
# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
# In this example:

# The non-zero numbers 1, 3, and 12 keep their relative order.
# The two zeros get moved to the end.
# Example 2
# Input: [2, 0, 4, 6, 0, 7]
# Output: [2, 4, 6, 7, 0, 0]
# Here, the zeros were originally in positions 1 and 4 (0-based indexing). After rearranging, all zeroes are at the end, while 2, 4, 6, and 7 maintain their original order relative to each other.

# Example 3
# Input: [0, 0, 1]
# Output: [1, 0, 0]
# Even if there are consecutive zeroes at the front, they should end up together at the back once you’ve moved them.

# Also read about the Python Program to Implementation of Linear Search in Python.

# Brute Force Solution
# Our main focus will be storing all the non-zeros elements in a seperate list/array and then change the first elements in original array with those numbers. We won’t be actually moving any zeros, but just replacing it. Let’s see how can we do this.

# Intuition and Approach
# The approach taken involves separating the non-zero elements from the zeros so that it makes us easy to rearrange the elements afterwards:

# Iterate the array and copy all non-zero elements into a temporary list called temp.
# Replace the beginning of the original array with the elements of temp, thus moving all non-zero elements to the front.
# Fill the remanining of the array with zeros, starting from the index where the non-zero elements end.
# This method makes sure that non-zero elements maintain their original sequence, and all zeros are pushed to the end of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        temp = []

        # Copy non-zero elements from original to temp array
        for i in range(n):
            if nums[i] != 0:
                temp.append(nums[i])

        # Number of non-zero elements
        nz = len(temp)

        # Copy elements from temp to fill first nz fields of original array
        for i in range(nz):
            nums[i] = temp[i]

        # Fill the rest of the cells with 0
        for i in range(nz, n):
            nums[i] = 0

# Optimal Solution (Using Two Pointers)
# We will be using two pointers named as i and j, to solve this solution. Have a look below and you will understand why this solution works and why this is optimal.

# Intuition and Approach
# The approach used here is the two-pointer technique to efficiently separate zero and non-zero elements:

# The first pointer, i, is used to find the first zero in the array.
# The second pointer, j, starts from i + 1 and is used to find the next non-zero element to swap with the zero at index i.
# This process continues, incrementally moving the i pointer each time a swap is made, effectively “collecting” non-zero elements at the start of the array and pushing zeros to the end.
# This method makes sure that the operations are done in-place, and by avoiding the use of extra storage or multiple passes, it optimizes both space and time efficiency.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                break
            i += 1
        else:
            return
        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1