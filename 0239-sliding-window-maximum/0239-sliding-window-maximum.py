from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        mDeque = deque([])

        for i in range(0, len(nums), 1):
            if len(mDeque) == 0:
                mDeque.append(nums[i])
            else:
                if (i - k) >= 0:
                    if mDeque[0] == nums[i - k]:
                        mDeque.popleft()
                while len(mDeque) > 0 and mDeque[-1] < nums[i]:
                    mDeque.pop()
                mDeque.append(nums[i])

            if i >= k - 1:
                result.append(mDeque[0])
        return result