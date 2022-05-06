class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) < k:
            return s
        stack = []
        for i in s:
            if not stack:
                stack.append([i, 1])
            else:
                if stack[-1][0] == i:
                    if stack[-1][1] + 1 == k:
                        stack.pop()
                    else:
                        stack[-1][1] += 1
                else:
                    stack.append([i, 1])
        result = ""
        for i in stack:
            result += i[0] * i[1]
        return result
        
            