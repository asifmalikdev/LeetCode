class Solution(object):

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def mergeSort(self, nums):
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)
        
    def findKthLargest(self, nums, k):
        nums = self.mergeSort(nums)
        return nums[-k]



nums = [3,2,1,5,6,4]
k = 2
obj = Solution()
print(obj.findKthLargest(nums, k))
        