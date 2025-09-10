class Solution(object):
    def findPermutationDifference(self, s, t):
        res = 0
        for i in range(len(s)):
            res = res + abs(s.index(s[i]) - t.index(s[i]))
        return res






s = "abc"
t = "bac"
obj = Solution()
print(obj.findPermutationDifference(s,t))