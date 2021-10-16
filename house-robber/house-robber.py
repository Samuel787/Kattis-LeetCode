class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for i in range(len(nums)):
            if i == 0:
                dp.append([nums[i], 0])
            elif i == 1:
                dp.append([nums[i], dp[i - 1][0]])
            elif i == 2:
                dp.append([nums[i] + dp[i - 2][0], dp[i - 1][0]])
            else:
                dp.append([nums[i] + max(dp[i - 2][0], dp[i - 2][1]), max(dp[i - 1][0], dp[i-1][1])])
                
        final_max = -1
        for i in range(len(dp)):
            temp_max = max(dp[i][0], dp[i][1])
            if temp_max > final_max:
                final_max = temp_max
        return final_max
        