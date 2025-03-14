class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        modifiedNums = [(nums[i], i) for i in range(len(nums))]
        modifiedNums.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            currSum = modifiedNums[l][0] + modifiedNums[r][0]
            if currSum == target:
                return [modifiedNums[l][1], modifiedNums[r][1]]
            elif currSum > target:
                r -= 1
            else:
                l += 1
        return [0, 0]


        