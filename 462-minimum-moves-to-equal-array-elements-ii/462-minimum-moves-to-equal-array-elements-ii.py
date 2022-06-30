class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median = 0
        size = len(nums)
        if size % 2 == 0:
            # median = (nums[size/2 - 1] + nums[size/2]) // 2
            temp = (nums[size/2 - 1] + nums[size/2]) / 2
            if temp % 1 == 0:
                median = temp // 1
            else:
                median = temp + .5
        else:
            median = nums[size // 2]
        steps = 0
        for num in nums:
            steps += abs(num - median)
        return steps
        