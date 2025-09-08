class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
            if len(s) > k:
                s.remove(nums[i - k])
        return False
        # mDict = {}
        # for i in range(len(nums)):
        #     curr = nums[i]
        #     if curr not in mDict:
        #         mDict[curr] = []
        #     if len(mDict[curr]) > 0:
        #         if i - mDict[curr][-1] <= k:
        #             return True
        #     mDict[curr].append(i)
        # return False

            