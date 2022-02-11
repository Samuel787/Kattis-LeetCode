class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        
        s1Dict = {}
        s2Dict = {}
        for c in string.lowercase:
            s1Dict[c] = 0
            s2Dict[c] = 0
        
        for c in s1:
            s1Dict[c] += 1
        
        length = len(s1)
        
        for i in range(0, length, 1):
            s2Dict[s2[i]] += 1
            
        matches = 0
        for key in s1Dict:
            if s1Dict[key] == s2Dict[key]:
                matches += 1
        if matches == 26:
            return True
        
        for toAddIndex in range(length, len(s2), 1):
            toRemoveIndex = toAddIndex - length
            charToRemove = s2[toRemoveIndex]
            charToAdd = s2[toAddIndex]
            if s2Dict[charToRemove] == s1Dict[charToRemove]:
                matches -= 1
            s2Dict[charToRemove] -= 1
            if s2Dict[charToRemove] == s1Dict[charToRemove]:
                matches += 1
            
            if s2Dict[charToAdd] == s1Dict[charToAdd]:
                matches -= 1
            s2Dict[charToAdd] += 1
            if s2Dict[charToAdd] == s1Dict[charToAdd]:
                matches += 1
            
            if matches == 26:
                return True
        
        return False
            