class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1]
        for i in range(1, len(nums), 1):
            output.append(output[i - 1] * nums[i - 1])
            
        back_prod = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            output[i] *= back_prod
            back_prod *= nums[i]
        return output