class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        partitions = []
        for letter in s:
            idx = -1
            for i in range(len(partitions)):
                if letter in partitions[i]:
                    idx = i
                    break
            newPartition = {}
            if idx == -1:
                # letter was not found in any partition, can create a new partition
                newPartition[letter] = 1
                partitions.append(newPartition)
            else:
                # merge partitions from idx to last partition
                for i in range(idx, len(partitions)):
                    currPartition = partitions[i]
                    for key in currPartition:
                        if key in newPartition:
                            newPartition[key] += currPartition[key]
                        else:
                            newPartition[key] = currPartition[key]
                newPartition[letter] += 1
                timesToPop = len(partitions) - idx
                for i in range(timesToPop):
                    partitions.pop()
                partitions.append(newPartition)

        result = []
        for partition in partitions:
            count = 0
            for key in partition:
                count += partition[key]
            result.append(count)
        return result