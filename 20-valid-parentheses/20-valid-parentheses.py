class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {")": "(", "]" : "[", "}" : "{"}
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if i == ")" or i == "]" or i == "}":
                    if len(stack) == 0:
                        return False
                    t = stack.pop()
                    if pairs[i] != t:
                        return False
        return len(stack) == 0
                    
                    