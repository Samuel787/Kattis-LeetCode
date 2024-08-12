class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.cache = {}
        return self.helper(nums, 0, 0, target)

    def helper(self, nums, index, curr_sum, target):
        if (index, curr_sum) in self.cache:
            return self.cache[(index, curr_sum)]
        
        if curr_sum == target and index == len(nums):
            return 1
        if index == len(nums):
            return 0
        
        curr = nums[index]
        additionWays = self.helper(nums, index + 1, curr_sum + curr, target)
        subtractionWays = self.helper(nums, index + 1, curr_sum - curr, target)
        self.cache[(index, curr_sum)] = additionWays + subtractionWays
        return self.cache[(index, curr_sum)]


