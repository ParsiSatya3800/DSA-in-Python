# http://codeanddebugacademy.com/bubble-sort-algorithm-in-python/

# nums=[7,6,5,4,3,2,1]
# class BubbleSort:
#     def BubbleSortAlgoritm(self,nums,n):
#         for i in range(n-2,-1,-1):
#             for j in range(0,i+1):
#                 if nums[j]>nums[j+1]:
#                     nums[j],nums[j+1]=nums[j+1],nums[j]
# BB=BubbleSort()
# BB.BubbleSortAlgoritm(nums,len(nums))
# print(nums)

nums=[7,6,5,4,3,2,1]
class BubbleSort:
    def BubbleSortAlgoritm(self,nums,n):
        for i in range(n-2,-1,-1):
            is_swap=False
            for j in range(0,i+1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    is_swap=True
        if is_swap==False:
            return True
BB=BubbleSort()
BB.BubbleSortAlgoritm(nums,len(nums))
print(nums)



                                            