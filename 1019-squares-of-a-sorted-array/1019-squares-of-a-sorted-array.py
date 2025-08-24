class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        left = 0
        right = 0
        for num in nums:
            if num < 0:
                right += 1
            else:
                break
        
        left = right - 1
        for i in range(left, -1, -1):
            nums[i] **= 2
        for i in range(right, len(nums), 1):
            nums[i] **= 2

        while len(res) != len(nums):
            if left == -1:
                while right < len(nums):
                    res.append(nums[right])
                    right += 1
            elif right == len(nums):
                while left >= 0:
                    res.append(nums[left])
                    left -= 1
            else:
                if nums[left] < nums[right]:
                    res.append(nums[left])
                    left -= 1
                else:
                    res.append(nums[right])
                    right += 1
        return res


        