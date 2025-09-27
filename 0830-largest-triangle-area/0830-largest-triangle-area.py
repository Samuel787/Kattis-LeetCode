class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0
        for i in range(0, len(points) - 2):
            for j in range(1, len(points) - 1):
                for k in range(2, len(points)):
                    A = points[i]
                    B = points[j]
                    C = points[k]
                    max_area = max(self.calculate_triangle_area(A, B, C), max_area)
        return max_area

    # adopts shoe lace formula for efficient calculation
    def calculate_triangle_area(self, pA, pB, pC):
        return 0.5 * abs(pA[0] * (pB[1] - pC[1]) + pB[0] * (pC[1] - pA[1]) + pC[0] * (pA[1] - pB[1]))