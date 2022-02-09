class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mDict = {}
        for i, num in enumerate(nums):
            if num in mDict:
                mDict[num] += 1
            else:
                mDict[num] = 1
        
        numPairs = 0
        
        for key in mDict:
            complement = k + key
            if complement == key:
                if mDict[complement] > 1:
                    numPairs += 1
            elif complement in mDict:
                numPairs += 1
        return numPairs