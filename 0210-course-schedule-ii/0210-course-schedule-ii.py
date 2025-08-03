class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.completed = []
        self.completedSet = set()
        self.graph = {}
        for i in range(numCourses):
            self.graph[i] = []

        for prereq in prerequisites:
            self.graph[prereq[0]].append(prereq[1])
        
        for course in self.graph:
            if self.dfs_cycle_detection(course, set()):
                return []
        return self.completed

    def dfs_cycle_detection(self, course, path):
        if course in path:
            return True
        if course in self.completedSet:
            return False
        
        path.add(course)
        for prereq in self.graph[course]:
            if self.dfs_cycle_detection(prereq, path):
                return True
        path.remove(course)

        self.completed.append(course)
        # print("This is completed: " + str(self.completed))
        self.completedSet.add(course)
        return False