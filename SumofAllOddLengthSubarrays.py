class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        res = 0
        prefix = [0] * (n + 1)      
        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]
        for i in range(n):
            for j in range(i+1, n+1): 
                if (j - i) % 2 == 1:  
                    res += prefix[j] - prefix[i]

arr = [1,4,2,5,3]
obj = Solution()
print(obj.sumOddLengthSubarrays(arr))