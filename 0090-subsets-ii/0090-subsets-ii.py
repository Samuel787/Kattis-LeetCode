class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        nums.sort()
        self.helper([], nums, 0)
        return self.result

    def helper(self, arr, nums, pointer):
        if pointer == len(nums):
            self.result.append(arr[::])
            return
        
        # include pointer's value
        newArr = arr[::]
        newArr.append(nums[pointer])
        self.helper(newArr, nums, pointer + 1)

        # exclude pointer's value
        val = nums[pointer]
        while pointer < len(nums) and nums[pointer] == val:
            pointer += 1
        self.helper(arr[::], nums, pointer)

