class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        count = target[0]
        for i in range(1, len(target)):
            count += max(0, target[i] - target[i - 1])
        return count