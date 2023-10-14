from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        mDeque = deque(result)

        # initialize initial window
        for i in range(k):
            if len(mDeque) == 0:
                mDeque.append(nums[i])
            else:
                while len(mDeque) > 0 and mDeque[-1] < nums[i]:
                    mDeque.pop()
                mDeque.append(nums[i])
        
        # print('1 => ' + str(list(mDeque)))
        result.append(mDeque[0])

        # count = 2
        currIdx = k
        while currIdx < len(nums):
            while len(mDeque) > 0 and mDeque[-1] < nums[currIdx]:
                mDeque.pop()
            # print("currIdx " + str(currIdx) + " ==> This the deque: " + str(mDeque))
            # print("This is the value of nums[idx -k]: " + str(nums[currIdx - k]))
            if len(mDeque) > 0 and (nums[currIdx - k]) == mDeque[0]:
                mDeque.popleft()
            mDeque.append(nums[currIdx])
            result.append(mDeque[0])
            # print(str(count) + " => " + str(list(mDeque))) 
            currIdx += 1
            # count += 1

        return list(result)