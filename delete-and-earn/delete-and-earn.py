class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = [0 for i in range(10001)]
        for i in nums:
            sums[i] += i
        
        dp = []
        dp.append(sums[1])
        dp.append(max(sums[1], sums[2]))
        for i in range(3, len(sums)):
            dp.append(max(sums[i] + dp[i - 3], dp[i - 2]))
            
        x = dp[9999]
        y = dp[9998]
        return max(x, y)