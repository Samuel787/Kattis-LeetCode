class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        freqMap = {}
        for i in s:
            if i in freqMap:
                freqMap[i] += 1
            else:
                freqMap[i] = 1
        isAddedMap = {}
        for key in freqMap:
            isAddedMap[key] = False
        res = ""
        for i in s:
            freqMap[i] -= 1
            if isAddedMap[i] == True:
                continue
                
            while (len(res) != 0 and res[-1] > i and freqMap[res[-1]] > 0):
                isAddedMap[res[-1]] = False
                res = res[:-1]
            res += i
            isAddedMap[i] = True
            
            # if res == "":
            #     res += i
            #     freqMap[i] -= 1
            #     isAddedMap[i] = True
            # else:
            #     while (len(res) != 0 and res[-1] > i and freqMap[res[-1]] > 0):
            #         isAddedMap[res[-1]] = False
            #         res = res[:-1]
            #     res += i
            #     isAddedMap[i] = True
            #     freqMap[i] -= 1
        
        return res
                    
                    