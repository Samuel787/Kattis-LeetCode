class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums.sort()
        i = len(nums) - 1
        j = len(nums) - 2
        k = len(nums) - 3
        while i > 1 and j > 0 and k > -1:
            if nums[k] + nums[j] > nums[i]:
                result = nums[k] +nums[j] + nums[i]
                break
            else:
                i -= 1
                j -= 1
                k -= 1

        return result
