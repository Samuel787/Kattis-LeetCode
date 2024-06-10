class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = heights[::]
        expected.sort()
        num = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                num += 1
        return num
        