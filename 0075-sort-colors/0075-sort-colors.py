class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        currPointer = 0
        for i in range(3):
            for j in range(currPointer, len(nums), 1):
                if nums[j] == i:
                    temp = nums[currPointer]
                    nums[currPointer] = nums[j]
                    nums[j] = temp
                    currPointer += 1
                    
        return nums

