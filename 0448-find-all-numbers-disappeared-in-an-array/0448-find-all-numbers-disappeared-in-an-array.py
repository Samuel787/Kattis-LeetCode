class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mSet = set()
        for num in nums:
            mSet.add(num)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in mSet:
                res.append(i)

        return res