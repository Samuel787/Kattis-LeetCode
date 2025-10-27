class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        prevCount = 0
        totalLasers = 0
        for row in bank:
            ones = self.countOnes(row)
            zeros = len(row) - ones
            if ones != 0:
                totalLasers += prevCount * ones
                prevCount = ones
        return totalLasers


    def countOnes(self, string):
        count = 0
        for i in string:
            if i == "1":
                count += 1
        return count
        