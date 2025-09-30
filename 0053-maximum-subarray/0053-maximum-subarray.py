class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = nums[0]
        maxSum = currSum
        for i in range(1, len(nums)):
            if currSum < 0:
                currSum = nums[i]
            else:
                currSum += nums[i]
            maxSum = max(maxSum, currSum)
        return maxSum