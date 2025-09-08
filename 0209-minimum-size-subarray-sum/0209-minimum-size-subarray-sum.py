class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        currSum = nums[0]
        l = 0
        r = 0
        if nums[0] == target:
            return 1
        
        minSize = len(nums) + 1
        while r < len(nums):
            # print("CurrSum is: " + str(currSum) + " l is: " + str(l) + " r is " + str(r) + " minSize: " + str(minSize))
            if currSum == target:
                minSize = min(minSize, r - l + 1)
                if minSize == 1:
                    return 1
                currSum -= nums[l]
                l += 1
                r += 1
                if r < len(nums):
                    currSum += nums[r]
            elif currSum < target:
                r += 1
                if r < len(nums):
                    currSum += nums[r]
            else:
                minSize = min(minSize, r - l + 1)
                currSum -= nums[l]
                l += 1
        if minSize > len(nums):
            return 0
        return minSize
            
             


            

        