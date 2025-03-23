class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = float('-inf')
        l = 0
        r = len(height)-1

        while l < r:
            maximum = max(maximum, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maximum
