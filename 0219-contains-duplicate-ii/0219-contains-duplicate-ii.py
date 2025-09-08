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
            mDict[curr].append(i)
        
        for val in mDict:
            arr = mDict[val]
            if len(arr) < 2:
                continue
            for i in range(0, len(arr) - 1, 1):
                if arr[i + 1] - arr[i] <= k:
                    return True
        return False
        
            