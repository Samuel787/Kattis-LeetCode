class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        spellList = []
        for i in range(len(spells)):
            spellList.append((spells[i], i))
        
        spellList.sort()

        potions.sort()

        pairs = [0 for _ in range(len(spells))]

        rightPtr = len(potions) - 1
        for sl in spellList:
            spell = sl[0]
            spellIdx = sl[1] # this is the ans idx

            while rightPtr >= 0 and spell * potions[rightPtr] >= success:
                rightPtr -= 1
            
            ans = len(potions) - 1 - rightPtr

            pairs[spellIdx] = ans

        return pairs

