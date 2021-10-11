class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        currMax, currMin = 1, 1
        for num in nums:
            temp = currMax
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(temp * num, currMin * num, num)
            res = max(currMax, res)
        return res