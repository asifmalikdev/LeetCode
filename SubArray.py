class Solution:
    def subArray(self, i, arr):
        # Base case: reached the end of the array, counts as 1 valid subsequence
        if i >= len(arr):
            return 1
        
        # Total = (count if we include arr[i]) + (count if we exclude arr[i])
        return self.subArray(i + 1, arr) + self.subArray(i + 1, arr)



obj = Solution()
arr = [1, 2, 3, 4]
sub_array = []
counter = 0
counter = obj.subArray(0, arr)
print(counter)
