class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.allCombinations = []
        self.generate("", n, n)
        return self.allCombinations

    def generate(self, result, openCount, closedCount):
        if openCount < 0:
            return
        if closedCount < 0:
            return
        if closedCount < openCount:
            # invalid path because must always be closedCount >= openCount
            return
        if openCount == 0 and closedCount == 0:
            self.allCombinations.append(result)
        self.generate(result + "(", openCount - 1, closedCount)
        self.generate(result + ")", openCount, closedCount - 1)