class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key=lambda x: x[1])
        max_time = 0
        heap = []
        for time, end_time in courses:
            heappush(heap, -time)
            max_time += time
            if max_time > end_time:
                big_time = heappop(heap)
                max_time += big_time
        return len(heap)