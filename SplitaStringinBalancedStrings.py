class Solution(object):
    def balancedStringSplit(self, s):
        res = 0
        res1 =0
        for char in s:
            if char =="L":
                res+=1
            else:
                res-=1
            if res == 0:
                res1+=1

        return res1
    
s = "LLLLRRRR"
obj = Solution()
print(obj.balancedStringSplit(s))