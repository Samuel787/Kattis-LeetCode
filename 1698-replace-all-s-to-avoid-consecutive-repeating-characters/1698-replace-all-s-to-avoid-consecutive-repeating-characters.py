class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        prev = None
        for i in range(len(s)):
            if s[i] != "?":
                result.append(s[i])
                continue
            
            if i != 0:
                prev = result[i - 1]

            if i == len(s) - 1:
                after = None
            else:
                after = s[i + 1]
            if s[i] == "?":
                if prev != "a" and after != "a":
                    result.append("a")
                elif prev != "b" and after != "b":
                    result.append("b")
                else:
                    result.append("c")
            else:
                result.append(s[i])
        res = "".join(result)
        return res
                    

        