class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        modulo = 10 ** 9 + 7
        
        for i in range(0, len(arr) - 2, 1):
            curr = arr[i]
            mMap = {}
            for j in range(i + 1, len(arr), 1):
                left = arr[j]
                complement = target - curr - left
                if complement in mMap:
                    result += mMap[complement]
                if arr[j] not in mMap:
                    mMap[arr[j]] = 0
                mMap[arr[j]] += 1
        return result % modulo
        