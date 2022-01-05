class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            curr = min(height[left], height[right]) * (right - left)
            if curr > area:
                area = curr
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return area