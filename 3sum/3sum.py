class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = set()
        nums.sort()
        for i in range(len(nums) - 2):
            curr_num = nums[i]
            target = -curr_num
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target:
                    results.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    left += 1
        return list(results)
        