class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        maxEnergy = None
        iterationWindow = min(k + 1, len(energy))
        for i in range(iterationWindow):
            curr = 0
            ptr = i
            while ptr < len(energy):
                # curr += energy[ptr]
                curr = max(energy[ptr], curr + energy[ptr])
                ptr += k
            if maxEnergy == None:
                maxEnergy = curr
            else:
                maxEnergy = max(maxEnergy, curr)
        return maxEnergy

        