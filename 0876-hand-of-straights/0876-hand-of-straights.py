class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        size = len(hand)
        if size % groupSize != 0:
            return False
        sortedHands = sorted(hand)
        expectedNumberGroups = size / groupSize
        currentGroups = 0
        nextStartPointer = 0
        isNextStartPointerSet = True
        prevCard = None
        currentIndex = 0
        # trying to form the desired number of groups
        while currentGroups < expectedNumberGroups:
            isNextStartPointerSet = False
            currentGroupSize = 0
            currentIndex = nextStartPointer
            debugger_current_group = []
            # trying to get 1 group from the remaining cards in the hand
            while currentGroupSize < groupSize and currentIndex < size:
                # current index is invalid
                if sortedHands[currentIndex] == -1:
                    currentIndex += 1
                    continue
                # start of a new group
                if prevCard == None:
                    prevCard = sortedHands[currentIndex]
                    debugger_current_group.append(prevCard)
                    sortedHands[currentIndex] = -1
                    currentGroupSize += 1
                    currentIndex += 1
                    continue
                # We have card [n] but there doesn't exist [n+1]. Instant fail
                if sortedHands[currentIndex] > prevCard + 1:
                    return False
                # Ideal case, we make use of the card in the current position
                elif sortedHands[currentIndex] == prevCard + 1:
                    prevCard = sortedHands[currentIndex]
                    debugger_current_group.append(prevCard)
                    sortedHands[currentIndex] = -1
                    currentGroupSize += 1
                    currentIndex += 1
                # We skip the card. Same card
                else:
                    if not isNextStartPointerSet:
                        isNextStartPointerSet = True
                        nextStartPointer = currentIndex
                    if currentIndex == size - 1:
                        return False
                    currentIndex += 1

            if not isNextStartPointerSet:
                nextStartPointer = currentIndex
            prevCard = None
            if currentGroupSize < groupSize:
                return False
            currentGroups += 1
        return currentGroups == expectedNumberGroups
                

                