class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        index = 1
        while index < len(intervals):
            if intervals[index][0] <= intervals[index - 1][1]:
                intervals[index - 1][1] = max(intervals[index][1], intervals[index - 1][1])
                intervals.pop(index)
            else:
                index += 1
        return intervals