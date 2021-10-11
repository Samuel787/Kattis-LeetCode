class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Greedy algorithm
        lastReachableIndex = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= lastReachableIndex:
                lastReachableIndex = i
        return lastReachableIndex == 0
        