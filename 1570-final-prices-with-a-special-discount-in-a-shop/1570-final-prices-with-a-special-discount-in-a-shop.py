class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        answer = [p for p in prices]

        stack = []
        for i in range(len(prices)):
            # each step we are comparing whatever is in the stack (came before) with the current price at [i]
            # and we greedily process it by clearing the stack as soon as we can
            while stack and prices[stack[-1]] >= prices[i]:
                top = stack.pop()
                answer[top] -= prices[i]
            
            stack.append(i)

        return answer
        