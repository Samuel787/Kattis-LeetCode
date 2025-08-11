class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        totalSum = 0
        for num in nums:
            totalSum += num
        if totalSum % 2 == 1:
            return False
        halfSum = totalSum / 2

        mSet = set()
        mSet.add(0)
        for num in nums:
            temp = []
            for i in mSet:
                newSum = i + num
                if newSum == halfSum:
                    return True
                temp.append(newSum)
            for i in temp:
                mSet.add(i)
        return False


        