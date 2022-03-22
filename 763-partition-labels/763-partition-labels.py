class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        mMap = {}
        for i in range(len(s)):
            mMap[s[i]] = i
        
        result = []
        start = 0
        end = 0
        for i in range(len(s)):
            if end == len(s) - 1:
                result.append(end - start + 1)
                break
            elif i == end:
                if start == end and mMap[s[i]] != i:
                        end = mMap[s[i]]
                else:
                    result.append(end - start + 1)
                    start = i + 1
                    end = i + 1
            else:
                if mMap[s[i]] > end:
                    end = mMap[s[i]]
        return result