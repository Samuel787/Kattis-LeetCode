class MyHashMap(object):
    
    prime = 769

    
    def __init__(self):
        self.hashmap = []
        for i in range(self.prime):
            self.hashmap.append([])
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        bucket = key % self.prime
        for i in self.hashmap[bucket]:
            if i[0] == key:
                i[1] = value
                return
        self.hashmap[bucket].append([key, value])

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        bucket = key % self.prime
        for i in self.hashmap[bucket]:
            if i[0] == key:
                return i[1]
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket = key % self.prime
        for i in range(len(self.hashmap[bucket])):
            if self.hashmap[bucket][i][0] == key:
                self.hashmap[bucket].pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)