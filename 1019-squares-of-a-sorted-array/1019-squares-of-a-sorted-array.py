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

        while len(res) != len(nums):
            if left == -1:
                while right < len(nums):
                    res.append(nums[right] ** 2)
                    right += 1
            elif right == len(nums):
                while left >= 0:
                    res.append(nums[left] ** 2)
                    left -= 1
            else:
                if nums[left] ** 2 < nums[right] ** 2:
                    res.append(nums[left] ** 2)
                    left -= 1
                else:
                    res.append(nums[right] ** 2)
                    right += 1
        return res


        