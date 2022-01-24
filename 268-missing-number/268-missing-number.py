class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0] != 0:
            return 0
        prev = None
        for num in nums:
            if prev == None:
                prev = num
            else:
                if num != prev + 1:
                    return prev + 1
                else:
                    prev = num
        return prev + 1
        