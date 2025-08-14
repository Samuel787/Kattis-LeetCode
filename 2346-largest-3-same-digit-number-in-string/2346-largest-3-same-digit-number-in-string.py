class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        if len(num) < 3:
            return ""
        bestVal = -1
        for start in range(len(num) - 2):
            if num[start] != num[start + 1]:
                continue
            if num[start + 1] != num[start + 2]:
                start += 1
                continue
            current = int(num[start])
            if current > bestVal:
                bestVal = current
        
        if bestVal == -1:
            return ""
        else:
            return str(bestVal) * 3
