class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trustedBy = {}
        trusting = {}
        for i in range(n):
            trustedBy[i + 1] = set()
            trusting[i + 1] = set()
        
        for t in trust:
            trustedBy[t[1]].add(t[0])
            trusting[t[0]].add(t[1])
        
        for p in trustedBy:
            if len(trustedBy[p]) == n - 1 and len(trusting[p]) == 0:
                return p
        
        return -1
