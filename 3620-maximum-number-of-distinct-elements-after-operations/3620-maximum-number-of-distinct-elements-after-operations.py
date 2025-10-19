class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # print("start sort")
        nums.sort()
        # print("end sort")
        prev = -float('inf')
        count = 0
        for i in range(len(nums)):
            if nums[i] + k <= prev:
                continue
            else:
                if nums[i] - k > prev:
                    prev = nums[i] - k
                else:
                    prev += 1
                count += 1
        return count