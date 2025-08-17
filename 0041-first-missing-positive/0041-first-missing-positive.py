class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        outOfBounds = len(nums) + 1
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            idx = abs(nums[i])
            if idx < 1 or idx > len(nums):
                continue
            idx -= 1
            if nums[idx] > 0:
                nums[idx] *= -1
            elif nums[idx] == 0:
                nums[idx] = -1 * outOfBounds
        
        for i in range(len(nums)):
            if nums[i] >= 0:
                return (i + 1)
        return len(nums) + 1

