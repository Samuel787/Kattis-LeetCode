class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if i == 0 or i == len(nums) - 1:
                continue
            # check if hill
            if nums[i - 1] < nums[i]:
                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i += 1
                if i != len(nums) - 1 and nums[i + 1] < nums[i]:
                    count += 1
            # check if valley
            if nums[i - 1] > nums[i]:
                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i += 1
                if i != len(nums) - 1 and nums[i + 1] > nums[i]:
                    count += 1
        return count