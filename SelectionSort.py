# https://codeanddebugacademy.com/python-program-for-selection-sort-algorithm/
nums=[7,2,3,5,1,6,4]
class Solution:
    def selectionsort(self,nums,n):
        for i in range(0,n):
            min_index=i
            for j in range(i+1,n):
                if nums[j]<nums[min_index]:
                    min_index=j
            nums[i],nums[min_index]=nums[min_index],nums[i]
s=Solution()
s.selectionsort(nums,len(nums))
print(nums)

# TC: O(n2)
# SC: O(1)
