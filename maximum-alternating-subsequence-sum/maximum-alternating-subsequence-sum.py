class Solution(object):
    
    
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.dp = {}
        self.nums = nums
        return self.dfs(0, True)
    
    def dfs(self, index, isEven):
        if index == len(self.nums):
            return 0
        if (index, isEven) in self.dp:
            return self.dp[(index, isEven)]
        
        if isEven:
            curr = self.nums[index]
        else:
            curr = -self.nums[index]
        self.dp[(index, isEven)] = max(curr + self.dfs(index + 1, not isEven), self.dfs(index + 1, isEven))
        return self.dp[(index, isEven)]
        
        