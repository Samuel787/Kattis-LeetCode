class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.result = []
        self.backtrack(0, [])
        return self.result
        
    def backtrack(self, start, path):
        self.result.append(path[:])
    
        if start >= len(self.nums):
            return

        for i in range(start, len(self.nums)):
            path.append(self.nums[i])
            self.backtrack(i + 1, path)
            path.pop()
        
    



        
