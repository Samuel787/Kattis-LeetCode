class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        circle = [(i + 1) for i in range(n)]

        while len(circle) > 1:
            for i in range(k):
                temp = circle.pop(0)
                if i != (k - 1):
                    circle.append(temp)
        return circle[0]