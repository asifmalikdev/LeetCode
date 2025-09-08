class Solution(object):
    def wordPattern(self, pattern, s):
        s = s.split()

        if len(pattern) != len(s):
            return False
        dict1 = {}
        for i in range(len(pattern)):
            if pattern[i] in dict1:
                if dict1[pattern[i]]  != s[i]:
                    return False
            else:
                if s[i] in dict1.values():
                    return False
                dict1[pattern[i]] = s[i]

        list1 = []
        for i in pattern:
            list1.append(dict1[i])

        return True if s==list1 else False

obj = Solution()
s = "dog cat cat dog"
p = "aaaa"
print(obj.wordPattern(p,s))