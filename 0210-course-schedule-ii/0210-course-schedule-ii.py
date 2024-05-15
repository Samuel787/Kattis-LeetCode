class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        #build the dependency graph as adjacency list
        self.graph = {}
        for i in range(numCourses):
            self.graph[i] = []
        for coursePair in prerequisites:
            self.graph[coursePair[0]].append(coursePair[1])
        
        self.visited = set()
        self.cycle = set()
        self.output = []
        # perform toposort on the graph
        for course in self.graph:
            if self.dfs(course) == False:
                return []
        return self.output

    
    def dfs(self, course):
        if course in self.cycle:
            return False
        if course in self.visited:
            return True
        
        self.cycle.add(course)
        for prereq in self.graph[course]:
            if self.dfs(prereq) == False:
                return False
        self.cycle.remove(course)
        self.visited.add(course)
        self.output.append(course)
        return True

