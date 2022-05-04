class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        leftIndex = 0
        rightIndex = len(nums) - 1
        numPairs = 0
        while leftIndex < rightIndex:
            currSum = nums[leftIndex] + nums[rightIndex]
            if currSum == k:
                numPairs += 1
                leftIndex += 1
                rightIndex -= 1
            elif currSum > k:
                rightIndex -= 1
            else:
                leftIndex += 1
        return numPairs
        