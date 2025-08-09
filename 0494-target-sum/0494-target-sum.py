class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.cache = {}
        self.target = target
        self.nums = nums
        return self.backtrack(0, 0)

    def backtrack(self, idx, curr_sum):
        if (idx, curr_sum) in self.cache:
            return self.cache[idx, curr_sum]

        if idx == len(self.nums):
            if curr_sum == self.target:
                return 1
            else:
                return 0
        
        
        self.cache[(idx, curr_sum)] = self.backtrack(idx + 1, curr_sum + self.nums[idx]) + self.backtrack(idx + 1, curr_sum - self.nums[idx])
        return self.cache[(idx, curr_sum)]