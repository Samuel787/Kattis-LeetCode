class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph = {}
        for course in range(numCourses):
            self.graph[course] = []
        
        for coursePair in prerequisites:
            self.graph[coursePair[0]].append(coursePair[1])

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
        for prereq in self.graph[course]:
            if self.dfs(prereq) == False:
                return False
        self.cycle.remove(course)
        self.visited.add(course)
        return True