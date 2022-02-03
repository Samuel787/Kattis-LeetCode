class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        count = 0
        self.dict = {}
        for i in nums1:
            for j in nums2:
                temp = i + j
                if temp not in self.dict:
                    self.dict[temp] = 1
                else:
                    self.dict[temp] += 1
        for i in nums3:
            for j in nums4:
                temp = -i - j
                if temp in self.dict:
                    count += self.dict[temp]
        return count