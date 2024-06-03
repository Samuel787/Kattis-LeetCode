class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(s) and ptr2 < len(t):
            if s[ptr1] == t[ptr2]:
                ptr2 += 1
            ptr1 += 1
        return len(t) - ptr2
        
        