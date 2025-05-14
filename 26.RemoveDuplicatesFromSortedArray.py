# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# 1. Brute Force Solution (With Dictionary)
# This approach will use dictionary to store unique elements and then use it to put it back into the original array. This might not be the most optimal solution, but we can still get to our answer.

# Intuition and Approach
# The solution uses a dictionary (my_dict) to track the unique elements of the array. Since dictionary keys in Python are unique, inserting each element of the array as a key in the dictionary automatically removes any duplicates. The approach is straightforward:

# Populate the dictionary with the elements of the array.
# Iterate through the dictionary keys, which are guaranteed to be unique, and copy them back into the original array nums.
# The new length of the array without duplicates is then the count of these unique keys.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_dict = dict()
        for i in nums:
            my_dict[i] = 0

        j = 0
        for n in my_dict:
            nums[j] = n
            j += 1
        return j
    

# 2. Optimal Solution (With Two Pointers)
# To solve this problem we will be using two pointers as i and j. Check out the solution below to understand what are we trying to do and understand through the images via dry run.

# Intuition and Approach
# Given that the array is sorted, our solution utilizes the two-pointer technique to effectively filter out duplicates in-place. The main idea is to maintain two pointers:

# i points to the last position of the unique elements encountered so far.
# j will loop through the array giving us non duplicates.
# If nums[j] is not equal to nums[i], it means nums[j] is a unique element that hasn’t been recorded yet. Therefore, nums[j] is swapped with nums[i+1], effectively growing the list of unique elements by one. The process ensures that all unique elements are shifted to the front of the array in their original order.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i = 0
        j = i + 1
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
        return i + 1