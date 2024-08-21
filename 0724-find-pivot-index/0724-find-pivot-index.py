class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.totalSum = 0
        for num in nums:
            self.totalSum += num
        
        self.leftSum = 0
        for i in range(len(nums)):
            self.totalSum -= nums[i]
            if self.leftSum == self.totalSum:
                return i
            self.leftSum += nums[i]
        return -1

