class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        
        SPECIAL_TOKEN = 10001
        prev =  nums[0]
        prevCount = 0
        for i in range(1, len(nums)):
            if nums[i] == prev:
                prevCount += 1
            else:
                prevCount = 0
                prev = nums[i]
            if prevCount > 1:
                nums[i] = SPECIAL_TOKEN
        
        # print(nums)
        
        xIndex = -1
        for i in range(len(nums)):
            if xIndex > i:
                i = xIndex
                continue
            if nums[i] == SPECIAL_TOKEN and xIndex == -1:
                xIndex = i
                continue
            if nums[i] != SPECIAL_TOKEN and xIndex != -1:
                nums[xIndex] = nums[i]
                nums[i] = SPECIAL_TOKEN
                for j in range(xIndex + 1, i + 1):
                    if nums[j] == SPECIAL_TOKEN:
                        xIndex = j
                        break
        
        numSpecialTokens = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == SPECIAL_TOKEN:
                numSpecialTokens += 1
            else:
                break
        
        return len(nums) - numSpecialTokens
                
            
            
                
        