class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        upperBound = int(math.sqrt(c))
        searchSpace = []
        for i in range(0, upperBound + 1, 1):
            searchSpace.append(i)
        
        left = 0
        right = len(searchSpace) - 1

        while left <= right:
            curr = searchSpace[left] * searchSpace[left] + searchSpace[right] * searchSpace[right]
            if curr == c:
                return True
            elif curr < c:
                left += 1
            else:
                right -= 1

        return False


        