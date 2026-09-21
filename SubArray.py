class Solution:
    def subArray(self, i, arr, sub_array):
        if i >= len(arr):
            print(sub_array)
            return
        sub_array.append(arr[i])
        self.subArray(i + 1, arr, sub_array)
        sub_array.pop()
        self.subArray(i+1,arr, sub_array)


obj = Solution()
arr = [1, 2, 3, 4]
sub_array = []
obj.subArray(0, arr, sub_array)
