class Solution():
    def merge(self, left_half, right_half):
        result = []
        i=j=0
        while i<len(left_half) and j<len(right_half):
            if left_half[i] < right_half[j]:
                result.append(left_half[i])
                i+=1
            else:
                result.append(right_half[j])
                j+=1
        
        result.extend(left_half[i:])
        result.extend(right_half[j:])
        
        return result


    def mergeSort(self, arr):
        if len(arr)<=1:
            return arr
        mid = len(arr)//2
        left_half  = self.mergeSort(arr[:mid])
        right_half = self.mergeSort(arr[mid:])
        return self.merge(left_half, right_half)        




arr = [38, 27, 43, 3, 9, 82, 10]
print(arr[:3])
print(arr[3:])
obj = Solution()
print(obj.mergeSort(arr))