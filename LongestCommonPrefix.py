class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort()
        print(strs)
        shortest_word_size = len(strs[0])
        
        prefix = ""
        for i in range(shortest_word_size):
            current_char = strs[0][i]
            for word in strs:
                if word[i] != current_char:
                    return prefix  

            prefix = prefix+ current_char  

        return prefix


strs = ["flower","flow","flight", "flee"]
x = ["flower","flow","flight", "flee"]
x.sort()
print(x)
obj = Solution()
print(obj.longestCommonPrefix(strs))