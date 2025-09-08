class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) < 3:
            return 0

        result = 0
        
        for i in range(1, len(arr) - 1, 1):
            l = i
            r = i
            while l > 0 and arr[l - 1] < arr[l]:
                l -= 1
            while r < len(arr) - 1 and arr[r] > arr[r + 1]:
                r += 1  
            if l != r and l != i and r != i:          
                curr = r - l + 1
                result = max(result, curr)
        
        return result

        