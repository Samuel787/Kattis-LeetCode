class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = path.split("/")
        stack = []
        for path in paths:
            if path == "..":
                if len(stack) != 0:
                    stack.pop()
            elif path == ".":
                continue
            elif path == "":
                continue
            else:
                stack.append(path)
                
        result = "/"
        for i in range(len(stack)):
            result += stack[i]
            if i != len(stack) - 1:
                result += "/"
            
        return result