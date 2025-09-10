class Solution(object):
    def firstUniqChar(self, s):
        dict1 = {}
        for ch in s:
            dict1[ch] = dict1.get(ch, 0) + 1
        
        for i, ch in enumerate(s):
            if dict1[ch] == 1:
                return i
        else:
            return -1
            
            
        


s ="loveleetcode"
obj = Solution()
print(obj.firstUniqChar(s))