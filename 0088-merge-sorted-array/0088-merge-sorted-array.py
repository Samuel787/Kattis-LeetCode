class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        currPtr = m + n - 1
        onePtr = m - 1
        twoPtr = n -1

        while onePtr >= 0 and twoPtr >= 0:
            if nums1[onePtr] > nums2[twoPtr]:
                nums1[currPtr] = nums1[onePtr]
                onePtr -= 1
            else:
                nums1[currPtr] = nums2[twoPtr]
                twoPtr -= 1
            currPtr -= 1
        
        while onePtr >= 0:
            nums1[currPtr] = nums1[onePtr]
            onePtr -= 1
            currPtr -= 1
        
        while twoPtr >= 0:
            nums1[currPtr] = nums2[twoPtr]
            twoPtr -= 1
            currPtr -= 1
        
        return nums1

                