class Solution(object):
    def countSegments(self, s):
        if len(s) < 1:
            return 0
        res = 0
        for i in range(len(s)):
            if s[i] == " " and (s[i-1] != " " or i == 0):
                res +=1
        return res
        
        




s = "Hello, my name is  John"
obj = Solution()
print(obj.countSegments(s))
