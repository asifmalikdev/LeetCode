from collections import Counter

class Solution(object):
    def isPossibleDivide(self, nums, k):
        freq = Counter(nums)
        for num in sorted(freq):
            while freq[num] > 0:
                for j in range(num, num+k):
                    if freq[j] <= 0:
                        return False
                    freq[j]-=1
        return True


nums = [3,2,1,2,3,4,3,4,5,9,10,11]
k =3
obj = Solution()
print(obj.isPossibleDivide(nums, k))