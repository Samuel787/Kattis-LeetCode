class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []

        intervals.sort()
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            prev = result[-1]
            curr = intervals[i]

            if curr[0] <= prev[1]:
                a = min(curr[0], prev[0])
                b = max(curr[1], prev[1])
                result[-1] = [a, b]
            else:
                result.append(curr)
        
        return result