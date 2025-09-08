class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        minDist = arr[1] - arr[0]
        result = [[arr[0], arr[1]]]
        for i in range(2, len(arr), 1):
            if arr[i] - arr[i - 1] < minDist:
                result = [[arr[i - 1], arr[i]]]
                minDist = arr[i] - arr[i - 1]
            elif arr[i] - arr[i -1] == minDist:
                result.append([arr[i-1], arr[i]])
        return result




        