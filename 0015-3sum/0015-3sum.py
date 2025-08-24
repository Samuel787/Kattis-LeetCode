class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = set()
        nums.sort()

        for i in range(len(nums) -2):
            left = i + 1
            right = len(nums) - 1
            target = -1 * nums[i]
            while left < right:
                curr = nums[left] + nums[right]
                if curr == target:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif curr > target:
                    right -= 1
                else:
                    left += 1
        return list(result)
                