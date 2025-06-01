class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 0:
            isEven = n % 2 == 0
            if not isEven:
                result += 1
            n = n >> 1
        return result