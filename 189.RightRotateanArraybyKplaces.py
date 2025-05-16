#Right Rotate an Array by K places

# 1. Brute Force Solution (Using Pop and Insert)
# This solution will contain pop method which removes the last element from the array and then use insert method to put the element at first. Doing so, we rotated our array by 1 time. Let’s see multiple rotations can lead to our answer.

# Intuition and Approach
# Given that rotating an array of length n by n times (or a multiple of n) results in the array looking the same as the original, the actual number of effective rotations needed is k % len(nums). This approach ensures the minimal number of steps required to achieve our result, optimizing performance when k is larger than len(nums).

# The logic we will apply is pretty simple:

# Determine the number of necessary rotations using k % len(nums).
# For each rotation, remove the last element of the array (nums.pop()) and insert it at the beginning (nums.insert(0, last)). This simulates a single right rotation.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Becuase if k = 8 and length = 7, means
        # we should only rotate 1 time instead of 8 times
        rotations = k % len(nums)

        for _ in range(rotations):
            last = nums.pop()
            nums.insert(0, last)

# 2. Better Solution (Using Slicing)
# This solution will contain slice method which is available in python to achieve our rotation and get our answer. You need to have a basic understanding of how slicing works in Python to understand the solution.

# Intuition and Approach
# The approach used here takes advantage of slicing in Python to rearrange segments of the array rather than manually moving elements. The core idea involves:

# Modifying k to be within the range of the array’s length using the modulus operation (k %= n). This handles cases where k is greater than the length of the array, reducing unnecessary full rotations.
# Slicing the array into two segments:
# The last k elements: nums[n-k:]
# The first n-k elements: nums[:n-k]
# Concatenating these two list/array in reverse order to achieve the desired right rotation.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        # Rotate the list in-place
        nums[:] = nums[n - k :] + nums[: n - k]

# 3. Optimal Solution (Using While Loop and Reversing Array)
# Before jumping on to this solution, please refer How to Reverse an Array using Loops.

# Intuition and Approach
# The approach we will apply uses reversals of array or a part of array to achieve the rotation without extra space for another array. The process is as follows:

# Normalize k to be less than the length of the array using k %= n. This handles cases where k is larger than the array size, reducing rotations.
# Reverse the last k elements of the array. This positions these elements as they should appear after a complete rotation.
# Reverse the first n-k elements. This prepares the front part of the array for a reversal.
# Reverse the entire array to finalize the positions of the elements for the right rotation.

class Solution:
    def reverse(self, nums: List[int], l: int, r: int) -> None:
        """
        Reverse the portion of nums starting at index l up to index r in-place.
        """
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Handle cases where k might be larger than n

        # 1. Reverse the last k elements
        self.reverse(nums, n - k, n - 1)

        # 2. Reverse the first n-k elements
        self.reverse(nums, 0, n - k - 1)

        # 3. Reverse the entire array
        self.reverse(nums, 0, n - 1)
