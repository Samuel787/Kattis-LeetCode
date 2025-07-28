class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        self.maximum = 0
        self.result = 0
        for num in nums:
            self.maximum |= num
        self.dfs(0, 0)
        return self.result
        

    def dfs(self, i, curr_max):
        if i == len(self.nums):
            if curr_max == self.maximum:
                self.result += 1
            return
        self.dfs(i + 1, curr_max | self.nums[i])
        self.dfs(i + 1, curr_max)
    

        