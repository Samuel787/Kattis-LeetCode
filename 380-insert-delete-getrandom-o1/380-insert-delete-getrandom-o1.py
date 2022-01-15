class RandomizedSet(object):
    

    def __init__(self):
        self.arr = []
        self.dict = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        self.arr.append(val)
        self.dict[val] = len(self.arr) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        index = self.dict[val]
        temp = self.arr[-1]
        self.arr[-1] = val
        self.arr[index] = temp
        self.dict[temp] = index
        self.arr.pop()
        self.dict.pop(val)
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        rand = random.randint(0, len(self.arr) - 1)
        return self.arr[rand]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()