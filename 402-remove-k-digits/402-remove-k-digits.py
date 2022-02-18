class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        myStack = []
        for c in num:
            if not myStack:
                myStack.append(c)
            else:
                while k > 0 and myStack and myStack[-1] > c:
                    myStack.pop()
                    k -= 1
                myStack.append(c)
        while k > 0 and myStack:
            myStack.pop()
            k -= 1
        result = ""
        
        while myStack and myStack[0] == "0":
            myStack.pop(0)
            
        for i in myStack:
            result += i
        
        if result == "":
            result = "0"
        return result