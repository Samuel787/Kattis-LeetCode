class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = set(["a", "e", "i", "o", "u"])
        vowelCount = {}
        consonantCount = {}
        maxVowel = 0
        maxConsonant = 0

        for c in s:
            if c in vowels:
                if c in vowelCount:
                    vowelCount[c] += 1
                else:
                    vowelCount[c] = 1
                if vowelCount[c] > maxVowel:
                    maxVowel = vowelCount[c]
            else:
                if c in consonantCount:
                    consonantCount[c] += 1
                else:
                    consonantCount[c] = 1
                if consonantCount[c] > maxConsonant:
                    maxConsonant = consonantCount[c]
            
        return (maxVowel + maxConsonant)
        