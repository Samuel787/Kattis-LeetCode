class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mDict = {}
        for i in range(len(nums)):
            if nums[i] not in mDict:
                mDict[nums[i]] = []
            mDict[nums[i]].append(i)
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement == nums[i]:
                if len(mDict[nums[i]]) > 1:
                    return [mDict[nums[i]][0], mDict[nums[i]][1]]
            elif complement in mDict:
                return [i, mDict[complement][0]]
        
        return []
                



        