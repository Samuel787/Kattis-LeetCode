class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            curr = min(height[left], height[right]) * (right - left)
            if curr > maxArea:
                maxArea = curr
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea