class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.nums = nums
        self.permutate(0)
        return self.result
    

    def permutate(self, start):
        if start == len(self.nums):
            self.result.append(self.nums[:])
            return
        
        # i is the index to swap with. 
        # start will be invariant for this loop
        for i in range(start, len(self.nums)):
            self.nums[start], self.nums[i] = self.nums[i], self.nums[start]
            # fix the start position and then find all the permutations for the remaining elements on the right in the arr
            self.permutate(start + 1)
            self.nums[start], self.nums[i] = self.nums[i], self.nums[start]
        
    
        