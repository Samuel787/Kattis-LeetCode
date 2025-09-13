class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        for num in nums:
            temp = []
            for j in output:
                deepcopy = [i for i in j]
                deepcopy.append(num)
                temp.append(deepcopy)
            output += temp
        return output