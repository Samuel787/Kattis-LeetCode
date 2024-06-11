class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        countMap = {}
        for num in arr1:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
        
        result = []
        for num in arr2:
            if num in countMap:
                totalCount = countMap[num]
                for i in range(totalCount):
                    result.append(num)
                countMap[num] = 0
        
        remaining = []
        for num in countMap:
            if countMap[num] != 0:
                for i in range(countMap[num]):
                    remaining.append(num)

        remaining.sort()
        for num in remaining:
            result.append(num)
        
        return result