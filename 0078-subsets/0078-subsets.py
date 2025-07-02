class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = [[]]
        for num in nums:
            currBatch = []
            for el in self.res:
                k = self.makeDeepCopy(el)
                k.append(num)
                currBatch.append(k)
            self.res += currBatch
        
        return self.res

    def makeDeepCopy(self, ll):
        k = []
        for i in ll:
            k.append(i)
        return k