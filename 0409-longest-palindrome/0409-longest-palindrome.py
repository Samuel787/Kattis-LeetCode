class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        countDict = {}
        for letter in s:
            if letter in countDict:
                countDict[letter] += 1
            else:
                countDict[letter] = 1

        maxLength = 0
        isOdd = False
        for letter in countDict:
            if countDict[letter] % 2 == 0:
                maxLength += countDict[letter]
            else:
                isOdd = True
                maxLength += countDict[letter] - 1
        if (isOdd):
            maxLength += 1
        
        return maxLength
