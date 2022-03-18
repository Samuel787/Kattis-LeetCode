class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        stack = []
        for i in s:
            if i == "(":
                stack.append(score)
                score = 0
            else:
                score = stack.pop() + max(score * 2, 1)
        return score
                       
        