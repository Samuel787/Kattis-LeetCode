class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums), 1):
            complement = target - nums[i]
            for j in range(i + 1, len(nums), 1):
                if nums[j] == complement:
                    return [i, j]
        return 0
                
        