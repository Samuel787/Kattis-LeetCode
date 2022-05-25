class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if len(envelopes) == 0:
            return 0
        
        '''
        Custom comparator function
        '''
        def compare(x, y):
            if x[0] == y[0]:
                return y[1] - x[1]
            else:
                return x[0] - y[0]
            
        result = 1
        envelopes.sort(cmp=compare)
        print(envelopes)
        dp = [0] * len(envelopes)
        maxlen = 0
        for i in range(len(envelopes)):
            index = self.binarySearch(dp, 0, maxlen, envelopes[i][1])
            dp[index] = envelopes[i][1]
            if index == maxlen:
                maxlen += 1
        return maxlen
        
    def binarySearch(self, dp, left, right, target):
        while left < right:
            mid = left + (right - left) / 2
            if dp[mid] == target:
                return mid
            elif dp[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left