from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]
        return s
       
        

s = ["hellox"]
print(len(s)//2)
#obj = Solution()
#print(obj.reverseString(s))
i = 3
s = ["h","e","l","l","o"]
print(-i-1)
print(s[-i-1])
print(s[-1])