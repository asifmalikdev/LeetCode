class Solution(object):
    def strStr(self, haystack, needle):
        print(haystack[0:3])
        for i in range(len(haystack)-len(needle)):
            if needle == haystack[i:i+(len(needle))]:
                return i
        



haystack = "sadbutsad"
needle = "sad"
obj = Solution()
print(obj.strStr(haystack, needle))