class Node:
    def __init__(self):
        self.children = {}
        self.maxIndex = 0

class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = Node()
        
        for i, word in enumerate(words):
            newWord = word + "#" + word
            for j in range(len(word)):
                cur = self.root
                for k in range(j, len(newWord)):
                    c = newWord[k]
                    if c not in cur.children:
                        cur.children[c] = Node()
                    cur = cur.children[c]
                    cur.maxIndex = i

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        index = -1
        cur = self.root
        for i in suffix:
            if i in cur.children:
                cur = cur.children[i]
            else:
                return -1
        if "#" not in cur.children:
            return -1
        cur = cur.children["#"]
        for i in prefix:
            if i in cur.children:
                cur = cur.children[i]
            else:
                return -1
        return cur.maxIndex


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)