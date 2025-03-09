class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        # we flatten the circle
        newColors = colors + colors[0:k - 1] # we append k - 1 of the starting elements
        print("new colors: ", newColors)
        count = 0
        i = 0
        while i < len(newColors):
            # cases:
            # 1. We try find an alternating group starting at i
            # 2. If we can find, we keep checking the next value until it hits end of newColors
            # 3. If we can't find, we update i to be the first break in the contiguous block
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
                # print("starting index: ", i)
                count += 1
                i += k
                while i < len(newColors):
                    curr = newColors[i]
                    if prev == curr:
                        break
                    else:
                        prev = curr
                        count += 1
                        # print("Another one starting at: ", i - k + 1)
                        i += 1

        return count
