class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(0, len(nums) - 1, nums, target)

    def binarySearch(self, left, right, nums, target):
        if left > right:
            return - 1
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return self.binarySearch(mid + 1, right, nums, target)
        else:
            return self.binarySearch(left, mid - 1, nums, target)
        