class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return max(nums)
        
        right = self.rob_1(nums[0:len(nums) - 1])
        left = self.rob_1(nums[1: len(nums)])
        return max(right, left)
        
    def rob_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        dp = []
        dp.append([nums[0], 0])
        dp.append([nums[1], nums[0]])
        max_val = max(nums)
        for i in range(2, len(nums)):
            # case where i rob this
            x = dp[i-1][1]
            y = dp[i - 2][0]
            z = dp[i - 2][1]
            rob = nums[i] + max(x, y, z)

            # case where i don't rob this
            x = dp[i-1][0]
            y = dp[i-1][1]
            w = dp[i-2][0]
            z = dp[i-2][1]
            dont_rob = max(x, y, w, z)
            
            dp.append([rob, dont_rob])
            if max(rob, dont_rob) > max_val:
                max_val = max(rob, dont_rob)
                
        return max_val