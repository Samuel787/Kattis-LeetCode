class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # idea, check if the graph contains any cycles

        # construct the adjacency graph of dependencies
        self.graph = {}
        self.completed = set()
        for course in range(numCourses):
            self.graph[course] = []

        for prereq in prerequisites:
            self.graph[prereq[0]].append(prereq[1])

        for course in self.graph:
            if course in self.completed:
                continue
            if not self.dfs(course, set()):
                return False
        return True
    
    def dfs(self, courseNum, visited):
        if courseNum in visited:
            print("Returning false")
            return False
        visited.add(courseNum)
        for course in self.graph[courseNum]:
            if course in self.completed:
                continue
            if not self.dfs(course, visited):
                # print("Returning false")
                return False
        # visited.remove(courseNum)
        self.completed.add(courseNum)
        return True