class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        result = []
        last_index_c = -1
        max_val = 10000
        for i in range(len(s)):
            if s[i] != c:
                if last_index_c == -1:
                    result.append(max_val)
                else:
                    diff = abs(i - last_index_c)
                    result.append(diff)
            else:
                last_index_c = i
                result.append(0)
                temp_i = i - 1
                while temp_i >= 0:
                    diff = abs(last_index_c - temp_i)
                    if result[temp_i] > diff:
                        result[temp_i] = diff
                    else:
                        break
                    temp_i -= 1
        return result