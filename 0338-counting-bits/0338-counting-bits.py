class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        if n == 0:
            return result
        result.append(1)
        powerLimit = 1 << 1
        reference = 2
        pointer = 2
        while len(result) < n + 1:
            if len(result) == powerLimit:
                reference = 0
                powerLimit = powerLimit << 1
            result.append(result[reference] + 1)
            # print("This is the reference: " + str(reference) + " and powerlimit: " + str(powerLimit) + " and appended: " + str(result[-1]))
            reference += 1
        
        return result

        