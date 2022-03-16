class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        while len(popped) > 0:
            if stack and popped[0] == stack[-1]:
                stack.pop()
                popped.pop(0)
            else:
                if len(pushed) == 0:
                    return False
                else:
                    stack.append(pushed.pop(0))
                    
        return len(stack) == 0