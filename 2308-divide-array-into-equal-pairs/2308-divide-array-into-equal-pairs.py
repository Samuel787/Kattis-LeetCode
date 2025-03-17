class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mDict = {}
        for num in nums:
            if num in mDict:
                mDict[num] += 1
            else:
                mDict[num] = 1
        
        for key in mDict:
            if mDict[key] % 2 != 0:
                return False
        return True