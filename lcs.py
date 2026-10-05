class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i,j = len(max(text1,text2)), len(min(text1,text2))
        print(i,j)
        tex1 = max(text1,text2)
        tex2 = min(text1,text2)
        counter = 0
        l = 0
        m = 0
        while m < i or l < i :
            print(tex1[l],tex2[m])
            if tex1[l] == tex2[m]:
                m+=1
                counter+=1
            l+=1
        return counter



obj = Solution()
res = obj.longestCommonSubsequence("abcd","acddd")
print(res)