class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        if len(p) > len(s):
            return result
        self.count_map = {}
        for letter in p:
            if letter in self.count_map:
                self.count_map[letter] += 1
            else:
                self.count_map[letter] = 1
        window_size = len(p)
        for i in range(0, window_size):
            if s[i] in self.count_map:
                self.count_map[s[i]] -= 1
        if self.checkFunction(self.count_map):
            result.append(0)
        for i in range(1, len(s) - window_size + 1):
            indexToRemove = i - 1
            indexToAdd = i + window_size - 1
            if s[indexToRemove] in self.count_map:
                self.count_map[s[indexToRemove]] += 1
            if s[indexToAdd] in self.count_map:
                self.count_map[s[indexToAdd]] -= 1
            if self.checkFunction(self.count_map):
                result.append(i)
                
            # print(str(i) + " map is " + str(self.count_map))
        return result
    
    def checkFunction(self, dictionary):
        for key in dictionary:
            if dictionary[key] != 0:
                return False
        return True
            
        