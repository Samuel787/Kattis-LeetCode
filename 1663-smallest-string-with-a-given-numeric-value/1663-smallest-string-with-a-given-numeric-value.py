class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        arr = []
        for i in range(n):
            arr.append(1)
            k -= 1
        
        for i in range(n):
            if k == 0:
                break
            elif k > 25:
                arr[i] += 25
                k -= 25
            else:
                arr[i] += k
                k = 0
        
        result = ""
        for i in range(len(arr) - 1, -1, -1):
            result += chr(arr[i] + 96)
        return result