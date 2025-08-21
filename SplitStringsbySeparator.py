class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        res = []
        for word in words:
            temp = word.split(separator)
            res+= [w for w in temp if w]
        return res
words = ["one.two.three","four.five","six"]
separator = "."
obj = Solution()
print(obj.splitWordsBySeparator(words, separator))