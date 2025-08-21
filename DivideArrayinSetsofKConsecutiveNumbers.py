from collections import Counter

class Solution(object):
    def isPossibleDivide(self, nums, k):
        # if (len(nums)-1) % k != 0:
        #     return False
        freq = Counter(nums)
        print(freq[2])


nums = [3,2,1,2,3,4,3,4,5,9,10,11]
k =3
obj = Solution()
print(obj.isPossibleDivide(nums, k))