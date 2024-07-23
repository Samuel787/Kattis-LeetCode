class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        countMap = {}
        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
            
        freqList = []
        for key in countMap.keys():
            freqList.append((countMap[key], key))
        key_func = functools.cmp_to_key(self.custom_comparator)
        freqList.sort(key = key_func)

        result = []
        for i in freqList:
            freq = i[0]
            for j in range(freq):
                result.append(i[1])
        return result
    
    def custom_comparator(self, a, b):
        if a[0] < b[0]:
            return -1
        elif a[0] > b[0]:
            return 1
        else:
            if a[1] < b[1]:
                return 1
            elif a[1] > b[1]:
                return -1
        return 0
        
        