class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        start = 0
        end = 0
        mDict = {}
        while end < len(s):
            curr = s[end]
            if curr not in mDict or mDict[curr] < start:
                mDict[curr] = end
                longest = max(longest, end - start + 1)
                print("End is: ", end)
                print("Start is: ", start)
            else:
                longest = max(longest, end - start)
                start = mDict[curr] + 1

                mDict[curr] = end
            end += 1
        return longest
        