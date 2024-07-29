class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.rotatedBinarySearch(0, len(nums) - 1, nums)
        
    
    def rotatedBinarySearch(self, left, right, nums):
        if left == right:
            return nums[left]
        if left == right - 1:
            return min(nums[left], nums[right])
        
        mid = (left + right) // 2
        if nums[mid] < nums[left]:
            return self.rotatedBinarySearch(left, mid, nums)
        else:
            # nums[mid] > nums[left]
            if nums[right] > nums[left]:
                return nums[left]
            else:
                return self.rotatedBinarySearch(mid + 1, right, nums)
