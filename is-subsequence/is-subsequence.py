class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) < len(s):
            return False
        s_idx = 0
        for i in range(len(t)):
            if t[i] == s[s_idx]:
                s_idx += 1
                if s_idx == len(s):
                    return True
        return s_idx == len(s)
                    
            