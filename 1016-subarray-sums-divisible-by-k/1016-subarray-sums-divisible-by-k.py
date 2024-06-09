class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        remainderMap = {}
        runningSum = 0
        for i in range(len(nums)):
            num = nums[i]
            runningSum += num
            remainder = runningSum % k
            if remainder in remainderMap:
                remainderMap[remainder].append(i)
            else:
                remainderMap[remainder] = [i]
        
        count = 0
        for key in remainderMap:
            length = len(remainderMap[key])
            count += (length * (length - 1)) / 2
            if key == 0:
                count += length
        
        return count

        