class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s)==sorted(t)
    

s = "anagram"
t = "nagaram"
obj = Solution()
print(obj.isAnagram(s,t))