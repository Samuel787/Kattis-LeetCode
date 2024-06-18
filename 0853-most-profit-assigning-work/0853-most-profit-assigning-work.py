from functools import cmp_to_key

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        # create a mapping of profit <--> difficulty and then sort by decreasing profit, ascending difficulty
        data = []
        for i in range(len(difficulty)):
            data.append((profit[i], difficulty[i]))

        key_function = cmp_to_key(self.compare)
        sorted_data = sorted(data, key=key_function)
        
        maxProfit = 0
        worker.sort(reverse=True)

        jobIdx = 0
        workerIdx = 0
        while workerIdx < len(worker) and jobIdx < len(difficulty):
            if worker[workerIdx] >= sorted_data[jobIdx][1]:
                maxProfit += sorted_data[jobIdx][0]
                workerIdx += 1
            else:
                # there is no worker who can do this job
                jobIdx += 1
        return maxProfit

    def compare(self, tuple1, tuple2):
        if tuple1[0] > tuple2[0]:
            return -1
        if tuple1[0] < tuple2[0]:
            return 1
        if tuple1[1] < tuple2[1]:
            return -1
        if tuple1[1] > tuple2[1]:
            return 1
        return 0

        

        
        