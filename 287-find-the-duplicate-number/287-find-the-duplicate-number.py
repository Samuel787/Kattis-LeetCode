class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while nums[i] != -1:
            temp = i
            i = nums[i]
            nums[temp] = -1
        return i