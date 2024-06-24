class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapOne = {}
        mapTwo = {}
        
        for letter in s:
            if letter in mapOne:
                mapOne[letter] += 1
            else:
                mapOne[letter] = 1

        for letter in t:
            if letter in mapTwo:
                mapTwo[letter] += 1
            else:
                mapTwo[letter] = 1

        if len(mapOne.keys()) != len(mapTwo.keys()):
            return False

        for key in mapOne:
            if key not in mapTwo or mapTwo[key] != mapOne[key]:
                return False
        return True
