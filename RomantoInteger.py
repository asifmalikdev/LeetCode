class Solution(object):
    def romanToInt(self, s):
        dict1 ={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,

        }
        temp = 0
        res = 0
        for i in range(len(s)-1, -1, -1):
            if dict1[s[i]] < temp:
                res = res - dict1[s[i]]
            else:
                res+=dict1[s[i]]
                temp = dict1[s[i]]
        return res
            


s = "LVIII"
obj = Solution()
print(obj.romanToInt(s))
        