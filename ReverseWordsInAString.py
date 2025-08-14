class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])



s = "this is asif"
obj = Solution()
print(obj.reverseWords(s))

        