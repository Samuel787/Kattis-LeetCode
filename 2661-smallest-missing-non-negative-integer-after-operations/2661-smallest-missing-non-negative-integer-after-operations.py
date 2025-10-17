class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        mDict = {}
        for i in nums:
            remainder = i % value
            if remainder not in mDict:
                mDict[remainder] = 0
            mDict[remainder] += 1

        mex = 0
        remainder = mex % value
        while remainder in mDict and mDict[remainder] > 0:
            mDict[remainder] -= 1
            mex += 1
            remainder = mex % value
        return mex