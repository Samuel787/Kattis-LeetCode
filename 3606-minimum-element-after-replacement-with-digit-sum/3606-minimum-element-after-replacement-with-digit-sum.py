class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = 10**4
        for num in nums:
            minimum = min(minimum, self.sumDigits(num))
        return minimum


    def sumDigits(self, num):
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total