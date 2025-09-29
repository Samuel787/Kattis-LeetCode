class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        self.dp = {}
        self.vertices = values
        return self.findMinScore(0, len(values) - 1)

    def findMinScore(self, i, j):
        if j < i + 2:
            return 0
        
        if (i, j) in self.dp:
            return self.dp[(i, j)]
        
        res = float('inf')
        for k in range(i + 1, j):
            res = min(res, self.vertices[i] * self.vertices[k] * self.vertices[j] + self.findMinScore(i, k) + self.findMinScore(k, j))
        self.dp[(i, j)] = res
        return res
        