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
        # print("This is the sorted list: " + str(sortedHands))
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
                # print("current start pointer: " + str(nextStartPointer) + "current group: " + str(debugger_current_group) + " current index: " + str(currentIndex))

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
                    # print("Returning false here: ")
                    self.print_list(debugger_current_group)
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
                        # print("Next start pointer is set at index: " + str(nextStartPointer))
                    if currentIndex == size - 1:
                        return False
                    currentIndex += 1
            # print("Full group here:")
            self.print_list(debugger_current_group)

            if not isNextStartPointerSet:
                nextStartPointer = currentIndex
            prevCard = None
            if currentGroupSize < groupSize:
                return False
            currentGroups += 1
        return currentGroups == expectedNumberGroups

    def print_list(self, mList):
        result = "["
        for i in mList:
            result += str(i)
        result += "]"
        print(result)
                

                