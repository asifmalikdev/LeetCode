from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        s1 = Counter(s1)
        print(Counter(s1))
        window = Counter(s2[:len(s1)])
        print(window)

s1 = "abc"
s2 = "ccccbbbbaaaa"
obj = Solution()
obj.checkInclusion(s1,s2)