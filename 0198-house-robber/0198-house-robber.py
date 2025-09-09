class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0, 0] for _ in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = nums[0]
            else:
                dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
                dp[i][1] = dp[i - 1][0] + nums[i]
        
        return max(dp[len(nums) - 1][0], dp[len(nums) - 1][1])