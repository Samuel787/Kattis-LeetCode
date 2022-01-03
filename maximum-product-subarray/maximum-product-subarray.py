class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = nums[0]
        min_product = nums[0]
        maximum = max_product
        for i in nums[1:]:
            temp_min = min_product
            min_product = min(i, min_product * i, max_product * i)
            max_product = max(i, temp_min * i, max_product * i)
            maximum = max(maximum, max_product)
        return maximum