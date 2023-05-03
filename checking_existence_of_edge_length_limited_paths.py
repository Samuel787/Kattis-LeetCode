class Solution(object):
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # parents = [-1 for i in range(n)]
        parents = list(range(n))

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            r1 = find(x)
            r2 = find(y)
            if r1 != r2:
                parents[r2] = r1
        
        edgeList.sort(key=lambda x:x[2])
        queries_sorted = [(i, u, v, l) for i, (u, v, l) in enumerate(queries)]
        queries_sorted.sort(key=lambda x:x[3])
        num_queries = len(queries)
        ans = [False] * num_queries
        edge_number = 0
        for index, u, v, limit in queries_sorted:
            while edge_number < len(edgeList) and edgeList[edge_number][2] < limit:
                union(edgeList[edge_number][0], edgeList[edge_number][1])
                edge_number += 1
            if find(u) == find(v):
                ans[index] = True
        return ans