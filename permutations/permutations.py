class Solution(object):
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        new_list = []
        for i in nums:
            temp = nums[:]
            temp.remove(i)
            permutations = self.permute(temp)
            if len(permutations) == 0:
                new_list += [[i]]
            else:
                for j in permutations:
                    new_list += [[i] + j]
        return new_list