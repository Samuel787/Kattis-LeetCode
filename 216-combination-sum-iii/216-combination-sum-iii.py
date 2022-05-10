class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.helper(1, k, n, [])
        return self.result
        
    def helper(self, start, k, n, currList):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            self.result.append([i for i in currList])
        
        for i in range(start, 10):
            currList.append(i)
            self.helper(i + 1, k - 1, n - i, currList)
            currList.pop()
        