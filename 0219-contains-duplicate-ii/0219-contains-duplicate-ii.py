class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # idea is to find if there are duplicates within a range of k
        mDict = {}
        for i in range(len(nums)):
            curr = nums[i]
            if curr not in mDict:
                mDict[curr] = []
            if len(mDict[curr]) > 0:
                if i - mDict[curr][-1] <= k:
                    return True
            mDict[curr].append(i)
        return False

            