class Solution(object):
    def getNoZeroIntegers(self, n):
        for i in range(1,n):
            a = i
            b = n-i
            res = []
            if a + b == n and "0" not in str(a) and "0" not in str(b):
                res.append(a)
                res.append(b)
                return res
            
    

num = 11
obj = Solution()
print(obj.getNoZeroIntegers(num))