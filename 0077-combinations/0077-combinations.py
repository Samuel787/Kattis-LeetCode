class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # self.space = [i for i in range(1, n + 1)]
        self.soln = []
        self.n = n
        self.k = k

        self.backtrack([], 1)
        return self.soln

    def backtrack(self, path, i):
        if len(path) == self.k:
            self.soln.append(path)
            return

        if i > self.n:
            return

        temp = path[:]
        temp.append(i)
        self.backtrack(path, i + 1)
        self.backtrack(temp, i + 1)
        


        
        