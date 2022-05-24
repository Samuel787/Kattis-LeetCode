class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        stack.append(-1)
        maxx = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    maxx = max(maxx, i - stack[-1])
        return maxx