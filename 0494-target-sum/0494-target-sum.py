class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        table = [{} for _ in range(len(nums) + 1)]
        table[0][0] = 1 # there is 1 way to get sum of 0 with 0 elements

        # for i in range(len(nums)):
        #     for curr_sum in table[i]:
        #         count = table[i][curr_sum]

        #         positiveSum = curr_sum + nums[i]
        #         negativeSum = curr_sum - nums[i]
            
        #         if positiveSum not in table[i + 1]:
        #             table[i + 1][positiveSum] = 0
        #         if negativeSum not in table[i + 1]:
        #             table[i + 1][negativeSum] = 0
                
        #         table[i + 1][positiveSum] += count
        #         table[i + 1][negativeSum] += count

        # return table[len(nums)][target]
        # i coded pethatically
        for i in range(0, len(nums)):
            row = table[i]
            for key in row:
                if (key - nums[i]) not in table[i + 1]:
                    table[i + 1][key - nums[i]] = 0
                table[i + 1][key - nums[i]] += table[i][key]
            
                if (key + nums[i]) not in table[i + 1]:
                    table[i + 1][key + nums[i]] = 0
                table[i + 1][key + nums[i]] += table[i][key]
        if target not in table[len(nums)]:
            return 0
        return table[len(nums)][target]
                
