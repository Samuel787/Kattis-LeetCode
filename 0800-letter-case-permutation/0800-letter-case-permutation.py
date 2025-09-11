class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.permutate(s)

        

    def permutate(self, substring):
        # print("Checking for " + substring)
        if len(substring) == 0:
            return []
        
        if len(substring) == 1:
            if not self.isChar(substring):
                return [substring]
            else:
                return [substring, self.getCompliment(substring)]
        
        current = substring[0]
        mList = self.permutate(substring[1:])
        newList = []
        for i in range(len(mList)):
            newList.append(current + mList[i])
        if self.isChar(current):
            complement = self.getCompliment(current)
            for i in range(len(mList)):
                newList.append(complement + mList[i])
        # print("returning: " + str(newList))
        return newList

        


        
        
    
    def isChar(self, a):
        return a.islower() or a.isupper()
    
    def getCompliment(self, a):
        if a.islower():
            return a.upper()
        elif a.isupper():
            return a.lower()
        else:
            return a


