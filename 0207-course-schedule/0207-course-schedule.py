class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph = {}
        for course in range(numCourses):
            self.graph[course] = set()
        
        for prereq in prerequisites:
            self.graph[prereq[0]].add(prereq[1])

        self.visited = set()
        self.cycle = set()
        for course in range(numCourses):
            if self.dfs(course) == False:
                return False
        return True

    def dfs(self, course):
        if course in self.visited:
            return True
        if course in self.cycle:
            return False

        self.cycle.add(course)
        for prereqCourse in self.graph[course]:
            if self.dfs(prereqCourse) == False:
                return False
        self.cycle.remove(course)
        self.visited.add(course)
        return True