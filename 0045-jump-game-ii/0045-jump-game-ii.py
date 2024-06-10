class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums)) == 1:
            return 0

        numberOfJumps = [(len(nums))] * len(nums)
        numberOfJumps[0] = 0
        initialJumps = 0
        
        for i in range(len(nums)):
            start = i + 1
            end = i + nums[i]
            for j in range(start, end + 1, 1):
                if j >= len(nums):
                    break
                numberOfJumps[j] = min(numberOfJumps[j], numberOfJumps[i] + 1)
                if j == len(nums) - 1:
                    return numberOfJumps[j]
        
        return numberOfJumps[-1]
        