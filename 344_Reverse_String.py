from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]
        return s
       
        

s = ["h"]
print(len(s)//2)
obj = Solution()
print(obj.reverseString(s))