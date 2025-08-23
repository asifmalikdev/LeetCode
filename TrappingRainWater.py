class Solution(object):
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0
        max_left = [0]*n
        max_right = [0]*n
        max_left[0] = height[0]

        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])
        
        max_right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            max_right[i] = max(height[i], max_right[i+1])

        
        traped = 0
        for i in range(n):
            traped+=min(max_left[i], max_right[i])-height[i]

        return traped

height = [0,1,0,2,1,0,1,3,2,1,2,1]
obj = Solution()
print(obj.trap(height))