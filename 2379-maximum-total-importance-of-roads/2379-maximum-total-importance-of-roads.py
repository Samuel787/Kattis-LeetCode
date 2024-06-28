class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adjList = {}
        for road in roads:
            cityOne = road[0]
            cityTwo = road[1]
            if cityOne in adjList:
                adjList[cityOne].append(cityTwo)
            else:
                adjList[cityOne] = [cityTwo]
            
            if cityTwo in adjList:
                adjList[cityTwo].append(cityOne)
            else:
                adjList[cityTwo] = [cityOne]
        
        tempArr = []
        for city in adjList:
            numConnectedCities = len(adjList[city])
            tempArr.append((numConnectedCities, city))
        
        tempArr.sort()

        # assign integer to city
        cityToIntegerMap = {}
        integer = n
        for i in range(len(tempArr) - 1, -1, -1):
            cityToIntegerMap[tempArr[i][1]] = integer
            integer -= 1
        
        maximumImportance = 0
        for road in roads:
            maximumImportance += cityToIntegerMap[road[0]] + cityToIntegerMap[road[1]]
        
        return maximumImportance
