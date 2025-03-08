class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -10**4
        cumSum = 0
        for num in nums:
            if num > (cumSum + num):
                cumSum = num
            else:
                cumSum += num
            res = max(cumSum, res)
        return res
        