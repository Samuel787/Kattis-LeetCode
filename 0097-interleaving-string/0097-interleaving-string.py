class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        self.cache = {}
        return self.dfs(0, 0, s1, s2, s3)
    
    def dfs(self, i, j, s1, s2, s3):
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        if i == len(s1) and j == len(s2):
            return True
        
        if i < len(s1) and s1[i] == s3[i + j] and self.dfs(i + 1, j, s1, s2, s3):
            return True
        if j < len(s2) and s2[j] == s3[i + j] and self.dfs(i, j + 1, s1, s2, s3):
            return True

        self.cache[(i, j)] = False
        # if len(s1) + len(s2) != len(s3):
        #     return False

        # curr = 0
        # s1Ptr = 0
        # s2Ptr = 0
        # while curr < len(s3):
        #     if s1Ptr < len(s1) and s2Ptr < len(s2) and s1[s1Ptr] == s2[s2Ptr] and s2[s2Ptr] == s3[curr]:
        #         if (self.isInterleave(s1[s1Ptr + 1:], s2[s2Ptr:], s3[curr + 1:])):
        #             return True
        #         else:
        #             return self.isInterleave(s1[s1Ptr:], s2[s2Ptr + 1:], s3[curr + 1:])
        #     elif s1Ptr < len(s1) and s3[curr] == s1[s1Ptr]:
        #         s1Ptr += 1
        #         curr += 1
        #     elif s2Ptr < len(s2) and s3[curr] == s2[s2Ptr]:
        #         curr += 1
        #         s2Ptr += 1
        #     else:
        #         return False
        # return True
            

                