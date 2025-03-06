class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.buckets = []
        self.cum = 0
        for weight in w:
            self.buckets.append([self.cum, self.cum + weight]) # Range: [cum, cum + weight)
            self.cum += weight
        
    def pickIndex(self):
        """
        :rtype: int
        """
        rand = random.randint(0, self.cum - 1)
        return self.findBucket(rand)


    def findBucket(self, rand):
        left = 0
        right = len(self.buckets) - 1
        while left <= right:
            mid = (left + right) // 2
            curr = self.buckets[mid]
            if rand >= curr[0] and rand < curr[1]:
                return mid
            elif rand >= curr[1]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()