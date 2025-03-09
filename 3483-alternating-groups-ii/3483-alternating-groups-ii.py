class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        newColors = colors + colors[0:k - 1]
        count = 0
        i = 0
        while i < len(newColors):
            hasFound = True
            prev = newColors[i]
            for j in range(i + 1, i + k, 1):
                if j >= len(newColors):
                    return count
                curr = newColors[j]
                if prev == curr:
                    i = j
                    hasFound = False
                    break
                else:
                    prev = curr
            if hasFound:
                count += 1
                i += k
                while i < len(newColors):
                    curr = newColors[i]
                    if prev == curr:
                        break
                    else:
                        prev = curr
                        count += 1
                        i += 1

        return count
