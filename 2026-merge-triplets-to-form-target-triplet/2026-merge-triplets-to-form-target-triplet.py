class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        res = set()
        for triple in triplets:
            shouldSkip = False
            for i in range(len(triple)):
                if triple[i] > target[i]:
                    shouldSkip = True
                    break
            if not shouldSkip:
                for i in range(len(triple)):
                    if triple[i] == target[i]:
                        res.add(i)
        return len(res) == 3

