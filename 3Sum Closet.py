class Solution():
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == target:
                    return total  # exact match is always the closest

                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total

                if total < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum

nums = [-1,2,1,-4]
target = 1
obj = Solution()
print(obj.threeSumClosest(nums, target))

