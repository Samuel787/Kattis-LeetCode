class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        mDict = {}
        nDict = {}
        for count in range(len(pattern)):
            letter = pattern[count]
            word = words[count]
            if letter in mDict:
                if mDict[letter] != word:
                    return False
            else:
                mDict[letter] = word
            if word in nDict:
                if nDict[word] != letter:
                    return False
            else:
                nDict[word] = letter
        return True