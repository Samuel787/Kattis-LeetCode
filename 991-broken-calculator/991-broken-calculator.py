class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        if startValue >= target:
            return startValue - target
        elif target % 2 == 0:
            return 1 + self.brokenCalc(startValue, target / 2)
        return 1 + self.brokenCalc(startValue, target + 1)
             
        
        