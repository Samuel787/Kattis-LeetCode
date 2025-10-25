class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = self.reduce(s)
        while len(temp) > 2:
            temp = self.reduce(temp)
        return temp[1] == temp[0]

    
    def reduce(self, s):
        res = ""
        for i in range(1, len(s)):
            res += str((int(s[i - 1]) + int(s[i])) % 10)
        return res
        