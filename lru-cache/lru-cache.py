class LRUCache(object):

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        # dummy pointers to head and tail
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.dict = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            # update the location to front of LL
            node = self.dict[key]
            # remove the link from the LL
            node.prev.next = node.next
            node.next.prev = node.prev
            # insert node in between head and next node
            self.head.next.prev = node
            node.next = self.head.next
            
            self.head.next = node
            node.prev = self.head
            return self.dict[key].val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return
        # check if full
        if key in self.dict:
            node = self.dict[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            
        elif len(self.dict) == self.capacity:
            # we evict least recently used from the back
            self.dict.pop(self.tail.prev.key)
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            
        # put it in front of LL
        node = self.Node(key, value)
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        self.dict[key] = node
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)