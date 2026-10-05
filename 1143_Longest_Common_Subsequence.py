def longestCommonSubsequence(text1: str, text2: str) -> int:
    memo = {}

    def dp(i: int, j: int) -> int:
        # Base case: if either string is exhausted
        if i == len(text1) or j == len(text2):
            return 0
        
        # Check cache
        if (i, j) in memo:
            return memo[(i, j)]
        
        # If characters match, move both pointers forward
        if text1[i] == text2[j]:
            memo[(i, j)] = 1 + dp(i + 1, j + 1)
        else:
            # If they don't match, try skipping a character in text1 or text2
            memo[(i, j)] = max(dp(i + 1, j), dp(i, j + 1))
            
        return memo[(i, j)]

    return dp(0, 0)


ans = longestCommonSubsequence("anc","acd")
print(ans)