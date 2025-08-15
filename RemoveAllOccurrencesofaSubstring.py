class Solution(object):
    def removeOccurrences(self, s, part):
        while part in s:
            s = s.replace(part, "",1)
        return s
            

    

s = "daabcbaabcbc"
part = "abc"
obj = Solution()
print(obj.removeOccurrences(s, part))