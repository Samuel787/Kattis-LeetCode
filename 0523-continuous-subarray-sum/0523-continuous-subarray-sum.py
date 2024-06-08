class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainderMap = {}
        remainderMap[0] = -1
        runningSum = 0
        for i in range(len(nums)):
            num = nums[i]
            runningSum += num
            remainder = runningSum % k
            if remainder in remainderMap:
                subarrayLength = i - remainderMap[remainder]
                if subarrayLength > 1:
                    return True
            else:
                remainderMap[remainder] = i
        return False

