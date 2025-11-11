class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.idxList = []

    def insert(self, val: int) -> bool:
        if val in self.hashMap and self.hashMap[val] != -1:
            return False
        self.idxList.append(val)
        self.hashMap[val] = len(self.idxList) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.hashMap or self.hashMap[val] == -1:
            return False
        
        idx = self.hashMap[val]
        
        # we save the lastElement
        lastElement = self.idxList[-1]
        self.hashMap[lastElement] = idx
        self.idxList[idx] = lastElement
    
        self.hashMap[val] = -1
        self.idxList.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.idxList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()