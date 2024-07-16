class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char
        s = new_s
        left = 0
        right = len(s) - 1
        while left <= right:
            if left == right:
                return True
            else:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
        return True