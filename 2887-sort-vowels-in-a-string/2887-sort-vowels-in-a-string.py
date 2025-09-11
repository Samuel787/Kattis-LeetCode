class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        vowelSet = set(vowels)

        collection = []
        for char in s:
            if char in vowelSet:
                collection.append(char)
        
        collection.sort()

        mString = []
        idx = 0
        for char in s:
            if char in vowelSet:
                mString.append(collection[idx])
                idx += 1
            else:
                mString.append(char)
        
        return "".join(mString)
        