class Solution(object):
    def findTheDifference(self, s, t):
        res = ""
        for ch in t:
            if t.count(ch) != s.count(ch):
                res = res+ch
        return res


s = "abcd"
t = "abcde"
obj = Solution()
print(obj.findTheDifference(s,t))