class Solution(object):
    
    phone = {}
    phone[2] = ["a", "b", "c"]
    phone[3] = ["d", "e", "f"]
    phone[4] = ["g", "h", "i"]
    phone[5] = ["j", "k", "l"]
    phone[6] = ["m", "n", "o"]
    phone[7] = ["p", "q", "r", "s"]
    phone[8] = ["t", "u", "v"]
    phone[9] = ["w", "x", "y", "z"]
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if len(digits) == 0:
            return result
        x = self.letterCombinations(digits[1:])
        for i in self.phone[int(digits[0])]:
            if len(x) == 0:
                result.append(i)
            else:
                for j in x:
                    result.append(i + j)
                
        return result
            