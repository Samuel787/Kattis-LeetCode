class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.helper(candidates, 0, target, [])
        
    def helper(self, candidates, index, target, path):
        if target == 0:
            return [path]
        elif target < 0:
            return [None]
        elif index >= len(candidates):
            return [None]
        
        result = []
        includePath = copy.deepcopy(path)
        includePath.append(candidates[index])
        include = self.helper(candidates, index, target - candidates[index], includePath)
        
        excludePath = copy.deepcopy(path)
        exclude = self.helper(candidates, index + 1, target, excludePath)
        
        if include:
            for res in include:
                if res != None:
                    result.append(res)
        if exclude:
            for res in exclude:
                if res != None:
                    result.append(res)
        return result