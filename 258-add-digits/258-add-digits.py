class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = self.helper(num)
        while result >= 10:
            result = self.helper(result)
        return result
        
    def helper(self, num):
        mSum = 0
        firstDigit = num % 10
        while num != 0:
            mSum += firstDigit 
            num = int(num / 10)
            firstDigit = num % 10
        return mSum