class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums
        while len(result) != 1:
            temp = []
            key = True
            for i in range(0, len(result), 2):
                if key:
                    temp.append(min(result[i], result[i + 1]))
                else:
                    temp.append(max(result[i], result[i + 1]))
                key = not key
            result = temp
        return result[0]
        