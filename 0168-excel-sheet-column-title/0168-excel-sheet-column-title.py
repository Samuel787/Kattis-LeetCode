class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = ""
        # generate the dictionary
        mDict = {}
        for i in range(1, 26):
            mDict[i] = chr(ord('A') + i - 1)
        mDict[0] = 'Z'
        
        while columnNumber > 0:
            digit = mDict[columnNumber % 26]
            res += digit
            columnNumber = (columnNumber - 1) // 26

        return res[::-1]
        # 26 -> Z
        # 27 -> AA
        # 28 -> AB
        # 52 -> AZ