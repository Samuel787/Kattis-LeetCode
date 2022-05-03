class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # check the left side
        leftIndex = 0
        for i in range(1, len(nums)):
            if nums[leftIndex] > nums[i]:
                break
            leftIndex += 1
        if leftIndex == len(nums) - 1:
            return 0
        print("This is the leftIndex: " + str(leftIndex))
        
        # check the right side
        rightIndex = len(nums) - 1
        for i in range(len(nums) -2, -1, -1):
            if nums[rightIndex] < nums[i]:
                break
            rightIndex -= 1
        print("This is the right Index: " + str(rightIndex))
        
        windowMax = max(nums[leftIndex:rightIndex + 1])
        windowMin = min(nums[leftIndex:rightIndex + 1])
        print("window min:" + str(windowMin) + "window max: " + str(windowMax))
        finalLeft = leftIndex
        while finalLeft >= 0 and nums[finalLeft] > windowMin :
            finalLeft -= 1
        finalLeft += 1
        
        finalRight = rightIndex
        while finalRight < len(nums) and nums[finalRight] < windowMax:
            finalRight += 1
        finalRight -= 1
        
        # print("This is the finalLeft: " + str(finalLeft))
        # print("This is the finalRight: " + str(finalRight))
        return finalRight - finalLeft + 1
    
        
             
        
        