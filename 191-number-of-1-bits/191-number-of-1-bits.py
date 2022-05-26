class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            if n % 2 == 0:
                n /= 2
            else:
                count += 1
                n -= 1
        return count
        