class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = max(nums)
        window = nums[0]
        for i in nums[1:]:
            if window < 0:
                window = i
            else:
                window += i
            max_sum = max(max_sum, window)
        return max_sum