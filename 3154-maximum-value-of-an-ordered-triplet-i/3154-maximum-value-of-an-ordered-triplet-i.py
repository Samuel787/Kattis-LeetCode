class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currMax = 0
        for i in range(0, len(nums) - 2, 1):
            for j in range(i + 1, len(nums) - 1, 1):
                for k in range(j + 1, len(nums), 1):
                    val = (nums[i] - nums[j]) * nums[k]
                    if val > currMax:
                        currMax = val
        return currMax