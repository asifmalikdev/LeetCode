class Solution(object):
    def isIsomorphic(self, s, t):
        dict1 = {}
        t = list(t)
        new_s =[]
        for i in range(len(s)):
            if s[i] not in dict1.keys() and t[i] not in dict1.values():
                dict1[s[i]] = t[i]
                new_s.append(t[i])
            elif s[i] in dict1.keys() and t[i] not in dict1.values(): 
                return False
            elif s[i] not in dict1.keys() and t[i] in dict1.values():
                return False
            else:
                if dict1[s[i]] == t[i]:
                    new_s.append(t[i])
        return True if new_s == t else False
    

    

s = "egg"
t = "add"
obj = Solution()
print(obj.isIsomorphic(s,t))
        


        