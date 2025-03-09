class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        mStack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                mStack.append(i)
            else:
                if len(mStack) == 0:
                    return False
                top = mStack.pop()
                if i == ")" and top != "(":
                    return False
                elif i == "]" and top != "[":
                    return False
                elif i == "}" and top != "{":
                    return False
        return len(mStack) == 0