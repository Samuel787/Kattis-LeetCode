class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        first = edges[0]
        second = edges[1]
        if first[0] == second[0] or first[0] == second[1]:
            return first[0]
        else:
            return first[1]
        