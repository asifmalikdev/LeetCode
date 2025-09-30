class Solution(object):
    def printVertically(self, s):
        words = s.split()
        max_length = max(len(word) for word in words)
        res = []

        for i in range(max_length):
            new_word = ""
            for word in words:
                if i < len(word):
                    new_word += word[i]
                else:
                    new_word += " "
            res.append(new_word.rstrip())
        return res




obj = Solution()
s = "TO BE OR NOT TO BE"
print(obj.printVertically(s))