class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = set()
        total_val = sum(nums)
        if total_val % 2 == 1:
            return False
        dp.add(0)
        half_val = total_val / 2
        for i in nums:
            temp_list = []
            for j in dp:
                if j + i == half_val:
                    return True
                temp_list.append(j + i)
            for j in temp_list:
                dp.add(j)
        return False
            
            
    