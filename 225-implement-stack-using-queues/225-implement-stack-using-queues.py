class MyStack(object):

    def __init__(self):
        self.queueOne = []
        self.queueTwo = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.queueOne) == 0:
            self.queueOne.append(x)
            while self.queueTwo:
                self.queueOne.append(self.queueTwo.pop(0))
        else:
            self.queueTwo.append(x)
            while self.queueOne:
                self.queueTwo.append(self.queueOne.pop(0))

    def pop(self):
        """
        :rtype: int
        """
        if self.queueOne:
            return self.queueOne.pop(0)
        else:
            return self.queueTwo.pop(0)

    def top(self):
        """
        :rtype: int
        """
        if self.queueOne:
            return self.queueOne[0]
        else:
            return self.queueTwo[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queueOne and not self.queueTwo
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()