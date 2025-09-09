class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mDict = {}
        for num in nums:
            if num not in mDict:
                mDict[num] = 0
            mDict[num] += 1
        
        result = []
        for key in mDict:
            result.append([mDict[key], key])
        
        result.sort()

        res = []
        for i in range(len(result) - 1, len(result) -1 - k, -1):
            res.append(result[i][1])
        
        return res