class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.result = 0
        self.getSubset([], 0, nums)
        return self.result

    def getSubset(self, arr, currIdx, nums):
        if currIdx == len(nums):
            self.result += self.getXORSum(arr)
            return
        # we try excluding currIdx
        self.getSubset(arr, currIdx + 1, nums)
        # we try including currIdx
        inc = [i for i in arr]
        inc.append(nums[currIdx])
        self.getSubset(inc, currIdx + 1, nums) 

    def getXORSum(self, arr):
        if len(arr) == 0:
            return 0
        curr = arr[0]
        for i in range(1, len(arr)):
            curr ^= arr[i]
        return curr
