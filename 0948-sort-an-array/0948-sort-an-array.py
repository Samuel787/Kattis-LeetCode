class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # convert all number to positive
        padding = 50000
        nums = [num + padding for num in nums]
        self.mergeSort(nums, 0, len(nums) - 1)
        nums = [num - padding for num in nums]
        return nums

    def mergeSort(self, nums, start, end):
        if (end - start) == 0:
            return nums
        
        mid = (start + end) // 2
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid + 1, end)
        return self.merge(nums, start, end)


    def merge(self, nums, start, end):
        mid = (start + end) // 2
        leftPointer = start
        rightPointer = mid + 1
        currPointer = start
        
        maxVal = max(nums[mid], nums[end]) + 1
        
        while leftPointer <= mid and rightPointer <= end and currPointer<= end:
            left = nums[leftPointer] % maxVal
            right = nums[rightPointer] % maxVal
            if left < right:
                nums[currPointer] += left * maxVal
                leftPointer += 1
            else:
                nums[currPointer] += right * maxVal
                rightPointer += 1
            currPointer += 1
        
        while leftPointer <= mid:
            nums[currPointer] += (nums[leftPointer] % maxVal) * maxVal
            currPointer += 1
            leftPointer += 1
        
        while rightPointer <= end:
            nums[currPointer] += (nums[rightPointer] % maxVal) * maxVal
            currPointer += 1
            rightPointer += 1
        
        for i in range(start, end + 1):
            nums[i] = nums[i] // maxVal
        return nums
        
    

