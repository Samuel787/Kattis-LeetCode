from math import gcd

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # check if there are any ones
        oneCount = nums.count(1)
        if oneCount:
            return len(nums) - oneCount
        
        # check if it is still possible
        g = 0
        for i in nums:
            g = gcd(g, i)
        if g > 1:
            return -1
        
        minLen = len(nums)
        for i in range(len(nums)):
            g = 0
            for j in range(i, len(nums)):
                g = gcd(g, nums[j])
                if g == 1:
                    minLen = min(minLen, j - i + 1)
                    break
        
        return minLen + len(nums) - 2

