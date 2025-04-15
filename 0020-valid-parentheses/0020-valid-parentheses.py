class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mStack = []
        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                mStack.append(bracket)
            elif bracket == ")":
                if not mStack or mStack.pop() != "(":
                    return False
            elif bracket == "]":
                if not mStack or mStack.pop() != "[":
                    return False
            elif bracket == "}":
                if not mStack or mStack.pop() != "{":
                    return False
        return len(mStack) == 0