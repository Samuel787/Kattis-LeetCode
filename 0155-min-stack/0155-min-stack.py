class MinStack:

    def __init__(self):
        self.mStack = []

    def push(self, val: int) -> None:
        if not self.mStack:
            self.mStack.append((val, val))
        else:
            currMin = self.mStack[-1][1]
            self.mStack.append((val, min(currMin, val)))        

    def pop(self) -> None:
        self.mStack.pop()

    def top(self) -> int:
        return self.mStack[-1][0]
        

    def getMin(self) -> int:
        return self.mStack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()