class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cache = set()
        for num in nums:
            if num in cache:
                return True
            cache.add(num)
        return False
        