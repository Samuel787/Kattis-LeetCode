class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        arr = [0 for i in range(7)]
        for i in tops:
            arr[i] += 1
        for i in bottoms:
            arr[i] += 1
            
        length = len(tops)
        targetNum = -1
        for i in range(len(arr)):
            if arr[i] >= length:
                targetNum = i
                break
        if targetNum == -1:
            return -1
        
        resultTop = 0
        resultBottom = 0
        for i in range(len(tops)):
            if tops[i] != targetNum:
                if bottoms[i] == targetNum:
                    resultTop += 1
                else:
                    return -1
            if bottoms[i] != targetNum:
                if tops[i] == targetNum:
                    resultBottom += 1
                else:
                    return -1
        return min(resultTop, resultBottom)
                    
        
        
        