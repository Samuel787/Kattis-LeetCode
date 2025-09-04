class Solution(object):
    def findClosest(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: int
        """
        distX = abs(z - x)
        distY = abs(z - y)
        if distX < distY:
            return 1
        elif distX > distY:
            return 2
        else:
            return 0        