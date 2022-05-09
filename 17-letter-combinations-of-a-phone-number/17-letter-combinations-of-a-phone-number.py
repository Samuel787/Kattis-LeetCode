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
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return self.phone[int(digits)]
        
        result = []
        # core logic
        for letter in self.phone[int(digits[0])]:
            for semi_result in self.letterCombinations(digits[1:]):
                result.append(letter + semi_result)
        
        return result
            