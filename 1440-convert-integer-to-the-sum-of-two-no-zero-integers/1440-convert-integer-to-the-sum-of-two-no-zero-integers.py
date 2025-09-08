class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        for i in range(1, n, 1):
            a = i
            b = n - a
            if "0" not in str(a) and "0" not in str(b):
                return [a, b]
        return []
        