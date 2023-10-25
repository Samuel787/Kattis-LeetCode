class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        hand.sort()
        count = 0
        next_ptr = 0
        curr_ptr = 0
        # print("hands at start: " + str(hand))
        while count < len(hand):
            curr_size = 0
            curr_ptr = next_ptr if next_ptr != -1 else curr_ptr

            # try to form a group
            # curr_group = [] # for debugging purposes
            prev = None
            while curr_size < groupSize and curr_ptr < len(hand):
                if hand[curr_ptr] == -1:
                    curr_ptr += 1
                    continue
                if prev == None:
                    prev = hand[curr_ptr]
                    # curr_group.append(hand[curr_ptr])
                    hand[curr_ptr] = -1
                    next_ptr = -1
                    # print("hands: " + str(hand))
                elif hand[curr_ptr] == prev + 1:
                    prev += 1
                    # curr_group.append(hand[curr_ptr])
                    hand[curr_ptr] = -1
                    # print("hands: " + str(hand))
                elif hand[curr_ptr] > prev + 1:
                    # we can't form a complete group currently
                    # print("Cannot form group: " + str(curr_group))
                    return False
                else:
                    # skip because hand[curr_ptr] == prev
                    if next_ptr == -1:
                        next_ptr = curr_ptr
                    curr_ptr += 1
                    continue
                curr_size += 1
                curr_ptr += 1
                count += 1

            if curr_size == groupSize:
                # print("found a complete group: " + str(curr_group))
                # print("now hands: " + str(hand))
                continue

            if curr_ptr == len(hand) and curr_size < groupSize:
                # print("Cannot form group: " + str(curr_group))
                return False

        return True