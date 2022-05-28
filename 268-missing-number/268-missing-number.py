class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        ex_sum = length * (length + 1) / 2
        for num in nums:
            ex_sum -= num
        return ex_sum
        