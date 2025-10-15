class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prevLength = 0
        currLength = 0
        doubleK = k * 2
        for i in range(len(nums)):
            if self.checkReturnCondition(prevLength, currLength, k, doubleK):
                return True

            if i == 0:
                currLength += 1
                continue
            if nums[i] <= nums[i - 1]:
                prevLength = currLength
                currLength = 1
            else:
                currLength += 1
        return self.checkReturnCondition(prevLength, currLength, k, doubleK)

    def checkReturnCondition(self, p, c, k, dk):
        return (p >= dk or c >= dk) or \
            (p >= k and c >= k)

        # if len(nums) == 2 and k == 1:
        #     return nums[0] >= nums[1]

        # for i in range(0, len(nums) - k):
        #     # print("Now checking idx: " + str(i))
        #     if i == 0:
        #         continue
            
        #     if nums[i] <= nums[i - 1]:
        #         # print("There is a discontinuity")
        #         cannotFindLeft = False
        #         # we scan left up to k
        #         print("Checking until the idx: " + str(i -k - 1))
        #         for j in range(i - 1, i - k - 1, -1):
        #             if j < 0:
        #                 # print("Cannot find on the left side because idx exceed")
        #                 cannotFindLeft = True
        #                 break
        #             if nums[j] <= nums[j - 1]:
        #                 # print("can find on the left side")
        #                 cannotFindLeft = True
        #                 break
        #         if cannotFindLeft:
        #             continue
                
        #         cannotFindRight = False
        #         # we scan right up to k

        #         for j in range(i+ 1, i + k):
        #             if j >= len(nums):
        #                 # print("Cannot find on the right side because idx exceed")
        #                 cannotFindRight = True
        #                 break
        #             if nums[j] <= nums[j - 1]:
        #                 # print("Cannot find on the right side")
        #                 cannotFindRight = True
        #                 break
                
        #         if not cannotFindRight and not cannotFindLeft:
        #             return True
        
        # return False

