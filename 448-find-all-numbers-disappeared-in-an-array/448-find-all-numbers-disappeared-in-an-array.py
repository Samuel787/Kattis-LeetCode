class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mSet = set(nums)
        result = []
        for i in range(1, len(nums) + 1):
            if i not in mSet:
                result.append(i)
        return result
        