# https://docs.google.com/document/d/1PRDubdMIyTeKf6QagCG2JF6QmpK28KkndvKQ70_dlEI/edit?tab=t.0
arr=[7,2,3,5,1,6,4]
class MergeSort:
    def merge_array(self,left,right):
        i=0
        j=0
        n=len(left)
        m=len(right)
        result=[]
        while i<n and j<m:
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        if i<n:
            while i<n:
                result.append(left[i])
                i+=1
        if j<m:
            while j<m:
                result.append(right[j])
                j+=1
        return result
    def MergeSortAlgorithm(self,arr):
        if len(arr)<=1:
            return arr
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]
        left_half=self.MergeSortAlgorithm(left_half)
        right_half=self.MergeSortAlgorithm(right_half)
        return self.merge_array(left_half,right_half)
    

MS=MergeSort()
arr1=MS.MergeSortAlgorithm(arr)
print(arr1)



