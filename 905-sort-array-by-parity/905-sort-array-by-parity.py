class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evenSlot = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                temp = nums[evenSlot]
                nums[evenSlot] = nums[i]
                nums[i] = temp
                evenSlot += 1
        return nums
        