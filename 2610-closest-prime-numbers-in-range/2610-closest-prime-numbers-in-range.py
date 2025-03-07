class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        sieve = self.getSieve(right)
        
        prev = -1
        curr = -1
        maximumDiff = 10 ** 6 + 1
        res = None
        for i in range(left, right + 1):
            if sieve[i]:
                if curr == -1:
                    curr = i
                else:
                    prev = curr
                    curr = i
                    
            if prev != -1:
                if (curr - prev) < maximumDiff:
                    res = [prev, curr]
                    maximumDiff = curr - prev
        if res == None:
            return [-1, -1]
        else:
            return res

    def getSieve(self, right):
        sieve = [True for i in range(right + 1)]
        sieve[0] = False
        sieve[1] = False
        for i in range(right + 1):
            if (i * i) > (right + 1):
                break
            if sieve[i]:
                j = i
                multiplier = 2
                while j * multiplier < (right + 1):
                    sieve[j * multiplier] = False
                    multiplier += 1
        return sieve