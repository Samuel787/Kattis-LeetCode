class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits) - 1, -1, - 1):
            digits[i] += carry
            if digits[i] >= 10:
                digits[i] %= 10
                carry = 1
            else:
                carry = 0
        if carry != 0:
            digits.insert(0, carry)
        return digits
