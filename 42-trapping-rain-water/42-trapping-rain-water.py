class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        total = 0
        while left < right:
            if height[left] <= max_right:
                left += 1
                max_left = max(height[left], max_left)
                total += max_left - height[left]
            else:
                right -= 1
                max_right = max(height[right], max_right)
                total += max_right - height[right]
        return total
                