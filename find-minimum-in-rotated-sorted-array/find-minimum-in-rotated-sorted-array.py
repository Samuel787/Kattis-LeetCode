class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (right + left) / 2
            if nums[mid] == nums[right]:
                return nums[right]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]