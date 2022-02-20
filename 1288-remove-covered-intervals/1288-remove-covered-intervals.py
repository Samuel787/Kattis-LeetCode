class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        curr = intervals[0]
        number = 1
        for interval in intervals[1:]:
            if interval[0] == curr[0] and interval[1] > curr[0]:
                curr = interval
            elif interval[1] <= curr[1]:
                continue
            else:
                curr = interval
                number += 1
        return number