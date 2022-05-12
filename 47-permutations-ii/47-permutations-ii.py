class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        
        countMap = {}
        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
        return self.helper(countMap)
        
    def helper(self, countMap):
        result = []
        for key in countMap:
            if countMap[key] != 0:
                countMap[key] -= 1
                partial_result = self.helper(countMap)
                countMap[key] += 1
                if len(partial_result) == 0:
                    result.append([key])
                else:
                    for x in partial_result:
                        x.append(key)
                        result.append(x)
        return result
                