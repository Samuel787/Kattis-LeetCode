class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            res.append(num)

        nums.sort()
        mDict = {}
        for i in range(len(nums)):
            if nums[i] not in mDict:
                mDict[nums[i]] = i

        for i in range(len(res)):
            res[i] = mDict[res[i]]
    
        return res
        


