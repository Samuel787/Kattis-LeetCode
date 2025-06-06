class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 0:
            n = n & (n - 1)
            result += 1
        return result