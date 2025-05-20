# https://docs.google.com/document/d/19clY4iP-9raJXFrUZlYA-sqUkCO0gf69F5-xBDDlxak/edit?tab=t.0
nums=[7,6,5,4,3,2,1]
class InsertionSort:
    def InsertionSortAlgoritm(self,nums,n):
        for i in range(1,n):
            j=i-1
            key=nums[i]
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j=j-1
            nums[j+1]=key
            
IS=InsertionSort()
IS.InsertionSortAlgoritm(nums,len(nums))
print(nums)