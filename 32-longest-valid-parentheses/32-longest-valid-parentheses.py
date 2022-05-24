class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxx = 0
        open = 0
        close = 0
        for i in s:
            if i == "(":
                open += 1
            else:
                close += 1
            if open == close:
                maxx = max(maxx, open + close)
            elif close > open:
                open = 0
                close = 0
                
        open = 0
        close = 0
        for i in reversed(s):
            if i == "(":
                open += 1
            if i == ")":
                close += 1
            if open == close:
                maxx = max(maxx, open + close)
            elif open > close:
                open = 0
                close = 0
        return maxx
    
    
        
        