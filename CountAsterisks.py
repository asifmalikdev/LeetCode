class Solution(object):
    def countAsterisks(self, s):
        sign = True
        res = 0
        for ch in s:
            if ch == "|":
                sign = not sign
            if sign:
                if ch == "*":
                    res+=1
        return res




obj = Solution()
s = "l|*e*et|c**o|*de|"
print(obj.countAsterisks(s))