class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        indicesToRemove = set()
        for i in range(1, len(words)):
            if self.areAnagrams(words[i-1], words[i]):
                indicesToRemove.add(i)

        result = []
        for i in range(len(words)):
            if i not in indicesToRemove:
                result.append(words[i])
        return result
        
    def areAnagrams(self, word1, word2):
        if len(word1) != len(word2):
            return False
        dictOne = self.getCountDict(word1)
        dictTwo = self.getCountDict(word2)
        if len(dictOne) != len(dictTwo):
            return False

        for l in dictOne:
            if l not in dictTwo:
                return False
            if dictOne[l] != dictTwo[l]:
                return False
        return True
    
    def getCountDict(self, word):
        dictOne = {}
        for l in word:
            if l not in dictOne:
                dictOne[l] = 1
            else:
                dictOne[l] += 1
        return dictOne