class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """

        mHeap = []
        heapq.heapify(mHeap)

        # we calculate the potential gain for each class and push it into the max heap
        for c in classes:
            p = c[0]
            t = c[1]
            gain = 0
            if p != t:
                gain = float(p + 1) / (t + 1) - float(p) / t
            heapq.heappush(mHeap, (-1 * gain, p, t))
        
        while extraStudents > 0:
            top = heapq.heappop(mHeap)
            p = top[1]
            t = top[2]
            newGain = 0
            if p != t:
                newGain = float(p + 2)/ (t + 2) - float(p + 1)/(t + 1)
            heapq.heappush(mHeap, (-1 * newGain, p + 1, t + 1))
            extraStudents -= 1

        avgPR = 0
        for c in mHeap:
            avgPR += float(c[1]) / c[2]

        return avgPR / float(len(classes))
    

        
        # for i in range(len(classes)):
        #     mClass = classes[i]
        #     heapq.heappush(mHeap, (mClass[0] / float(mClass[1]), i))
        
        # while extraStudents > 0:
        #     top = heapq.heappop(mHeap)
        #     idx = top[1]
        #     print("This is current class with lowest ratio: " + str(classes[idx]))
        #     classes[idx][0] += 1
        #     classes[idx][1] += 1
        #     extraStudents -= 1
        #     heapq.heappush(mHeap, (classes[idx][0] / float(classes[idx][1]), idx))
        
        # sumPassRatio = 0
        # for i in classes:
        #     sumPassRatio += i[0] / float(i[1])
        # return sumPassRatio / len(classes)
            