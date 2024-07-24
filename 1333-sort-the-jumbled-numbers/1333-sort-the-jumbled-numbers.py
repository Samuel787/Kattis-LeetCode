class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stringNums = [str(num) for num in nums]
        
        letterMapping = {}
        for i in range(len(mapping)):
            letterMapping[str(i)] = str(mapping[i])
        
        wordMapping = {}
        mappedStringNums = []
        for stringNum in stringNums:
            mappedNum = ""
            for digit in stringNum:
                mappedNum += letterMapping[digit]
            mappedStringNums.append(mappedNum)
            wordMapping[mappedNum] = stringNum

        actualNumberToMappedString = {}
        for mappedStringNum in mappedStringNums:
            integerVal = int(mappedStringNum)
            if integerVal in actualNumberToMappedString:
                actualNumberToMappedString[integerVal].append(mappedStringNum)
            else:
                actualNumberToMappedString[integerVal] = [mappedStringNum]

        mappedActualNums = [int(num) for num in mappedStringNums]
        mappedActualNums.sort()

        result = []
        for actualNumber in mappedActualNums:
            stringVal = actualNumberToMappedString[actualNumber][0]
            del actualNumberToMappedString[actualNumber][0]
            result.append(int(wordMapping[stringVal]))
        
        return result

        