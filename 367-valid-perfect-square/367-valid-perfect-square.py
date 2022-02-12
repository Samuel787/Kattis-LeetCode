class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 0
        end = num
        
        while start <= end:
            mid = (start + end) / 2
            midSquare = mid ** 2
            
            if midSquare == num:
                return True
            elif midSquare > num:
                end = mid - 1
            else:
                start =  mid + 1
        return False
            