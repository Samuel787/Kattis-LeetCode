class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [0] * len(temperatures)
        curr_index = -1
        for temp in temperatures:
            curr_index += 1
            while stack and temp > stack[-1][0]:
                pos = stack[-1][1]
                result[pos] = curr_index - pos
                stack.pop()
            stack.append((temp, curr_index))
        return result