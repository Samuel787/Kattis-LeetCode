class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0

        while res < n:
            res = res << 1
            res += 1

        return res
        