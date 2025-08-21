class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        totalSum = (count * (count + 1)) // 2
        for num in nums:
            totalSum -= num
        return totalSum
        