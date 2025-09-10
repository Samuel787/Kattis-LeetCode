class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = []
        postfix = [-1 for _ in nums]
        prod = 1
        for num in nums:
            prod *= num
            prefix.append(prod)
            
        
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            postfix[i] = prod
        
        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(postfix[i + 1])
            elif i == len(nums) - 1:
                result.append(prefix[i - 1])
            else:
                result.append(prefix[i - 1] * postfix[i + 1])
        
        return result
