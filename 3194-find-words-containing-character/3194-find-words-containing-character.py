class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        res = []
        idx= 0 
        for word in words:
            for i in word:
                if i == x:
                    res.append(idx)
                    break
            idx += 1
        return res

        