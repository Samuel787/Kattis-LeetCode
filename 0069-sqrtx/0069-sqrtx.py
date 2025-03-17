class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # we do binary search liao
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            sq = mid * mid
            if sq > x:
                high = mid - 1
            elif sq < x:
                t = (mid + 1) ** 2
                if t == x:
                    return (mid + 1)
                elif t > x:
                    return mid
                else:
                    low = mid + 1
            else:
                return mid
        return 0
        