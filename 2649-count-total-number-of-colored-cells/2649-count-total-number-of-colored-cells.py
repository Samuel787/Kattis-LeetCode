class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        curr = 1
        for minute in range(1, n):
            curr += minute * 4
        return curr        