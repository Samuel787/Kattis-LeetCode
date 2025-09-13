class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # self.space = [i for i in range(1, n + 1)]
        space = [[]]
        soln = []
        for i in range(1, n + 1):
            temp = []
            for j in space:
                deepcopy = [m for m in j]
                deepcopy.append(i)
                # print("This is deepcopy: " + str(deepcopy))
                if len(deepcopy) == k:
                    # print("Adding this deepcopy: " + str(deepcopy))
                    soln.append(deepcopy)
                else:
                    temp.append(deepcopy)
            space += temp
        
        return soln

        
        