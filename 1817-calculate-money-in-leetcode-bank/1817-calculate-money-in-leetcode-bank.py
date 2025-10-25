class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        mondayCount = 0
        total = 0
        prev = 0
        for i in range(n):
            if i % 7 == 0:
                mondayCount += 1
            
            total += mondayCount
            total += i % 7
        return total
            
                

        