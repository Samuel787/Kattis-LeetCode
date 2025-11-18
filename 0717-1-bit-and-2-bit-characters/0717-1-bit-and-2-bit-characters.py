class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx = 0
        while idx < len(bits) - 1:
            if bits[idx] == 0:
                idx += 1
            else:
                idx += 2
        return idx == len(bits) - 1


        # only need to check the last 3 bits
        if len(bits) == 1:
            return bits[-1] == 0
        if len(bits) == 2:
            return bits[0] == 0
        checkBits = str(bits[-3]) + str(bits[-2])
        # print("This is checkBits: " + str(checkBits))
        return checkBits == "00" or checkBits == "10" or checkBits == "11"

        '''
        000 -> true
        010 -> false
        100 -> true
        110 -> false
        '''
