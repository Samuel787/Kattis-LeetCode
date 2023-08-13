class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        right = left
        maxLength = 0
        lastIndex = len(s) - 1
        lengthOfS = len(s)
        counts = {}
        while left < len(s) and right < len(s):
            newChar = s[right]
            if newChar in counts:
                counts[newChar] += 1
            else:
                counts[newChar] = 1
            
            maxCount = self.getMaxCountInDict(counts)

            currWindowLength = right - left + 1
            if currWindowLength - maxCount <= k:
                # print("left: " + str(left) + " right: " + str(right) + " currWindowLength: " + str(currWindowLength) + " maxCount: " + str(maxCount))
                maxLength = max(maxLength, currWindowLength)
            else:
                # print("left: " + str(left) + " right: " + str(right) + " currWindowLength: " + str(currWindowLength) + " maxCount: " + str(maxCount))
                counts[s[left]] -= 1
                left += 1
                if left < lastIndex:
                    currWindowLength -= 1
                    newMaxCount = self.getMaxCountInDict(counts)
                    if currWindowLength - newMaxCount <= k:
                        maxLength = max(maxLength, currWindowLength)
            right += 1

        while left < len(s):
            counts[s[left]] -= 1
            left += 1
            maxCount = self.getMaxCountInDict(counts)

            currWindowLength = right - left + 1
            if currWindowLength - maxCount <= k:
                maxLength = max(maxLength, currWindowLength)
        return maxLength

    
    def getMaxCountInDict(self, mDict):
        currMax = 0
        for key in mDict:
            currMax = max(currMax, mDict[key])
        return currMax
