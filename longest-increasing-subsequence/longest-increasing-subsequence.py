class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1 for i in range(len(nums))]

        for i in range(len(nums) - 2, -1, -1):
            max_val = 1
            for j in range(i + 1, len(nums), 1):
                if (nums[i] < nums[j]) and (dp[j] + dp[i] > max_val):
                    max_val = dp[i] + dp[j]
            dp[i] = max(max_val, dp[i])
        return max(dp)
            