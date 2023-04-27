class Solution(object):
    def bulbSwitch(self, n):
        count = 0
        square = 1
        while square <= n:
            count += 1
            square = (count + 1) * (count + 1)
        return count