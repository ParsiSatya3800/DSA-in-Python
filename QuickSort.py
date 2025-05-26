# # https://docs.google.com/document/d/19fWIYQ3Nz3fS0OvXL5Z8JBFB9ya87pmEmvDdaANLHdM/edit?tab=t.0
# nums=[7,2,3,5,1,6,4]
# class QuickSort:
#     def partition(self,nums,low,high):
#         pivot=nums[low]
#         i=low+1
#         j=high-1
#         while(i<j):
#             while nums[i]>=pivot and i<=high-1:
#                 i+=1
#             while nums[j]<pivot and j>=low+1:
#                 j+=1
#             if i<j:
#                 nums[j],nums[pivot]=nums[pivot],nums[j]
#         return j
#     def QuickSortAlgorithm(self,nums,low,high):
#         if low<high:
#             p_ind=self.partition(nums,low,high)
#             self.QuickSortAlgorithm(nums,low,p_ind)
#             self.QuickSortAlgorithm(nums,p_ind+1,high)

# QS=QuickSort()
# QS.QuickSortAlgorithm(nums,0,len(nums))
# print(nums)

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1

        while arr[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low < high:
        p_index = partition(arr, low, high)
        quick_sort(arr, low, p_index - 1)
        quick_sort(arr, p_index + 1, high)
arr = [64, 34, 25, 12, 22, 12, 12, 11, 90]
quick_sort(arr, 0, len(arr) - 1)
print(f"Sorted array = {arr}")