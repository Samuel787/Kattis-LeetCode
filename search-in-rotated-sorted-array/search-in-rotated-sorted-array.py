class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            print("mid: " + str(mid) + " val is: " + str(nums[mid]))
            if nums[mid] > nums[right]:
                left = mid
                right -= 1
            elif nums[mid] > nums[left]:
                left = mid
            elif nums[mid] < nums[left]:
                right = mid - 1
            elif nums[mid] < nums[right]:
                if nums[right] > nums[left]:
                    left = right
                else:
                    right = mid - 1
        peak = left
        if target >= nums[0]:
            return self.binary_search(nums, 0, peak, target)
        else:
            return self.binary_search(nums, peak + 1, len(nums) - 1, target)
        
    def binary_search(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return - 1
                
        