class FreqStack(object):

    def __init__(self):
        self.freqMap = {}
        self.freqStack = {}
        self.maxFreq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.freqMap:
            self.freqMap[val] += 1
        else:
            self.freqMap[val] = 1
        if self.freqMap[val] > self.maxFreq:
            self.maxFreq = self.freqMap[val]
        if self.maxFreq not in self.freqStack:
            self.freqStack[self.maxFreq] = []
        self.freqStack[self.freqMap[val]].append(val)

    def pop(self):
        """
        :rtype: int
        """
        result = self.freqStack[self.maxFreq].pop()
        if len(self.freqStack[self.maxFreq]) == 0:
            self.maxFreq = max(self.maxFreq - 1, 0)
        self.freqMap[result] -= 1
        return result
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()