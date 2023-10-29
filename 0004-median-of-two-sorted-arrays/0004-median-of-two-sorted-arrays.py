class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        half = total // 2

        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A # ensure smaller arr is A
        
        l, r = 0, len(A) - 1
        
        while True:
            mid = (l + r) // 2 # A
            j = half - (mid + 1) - 1 # B

            aLeft = A[mid] if mid >= 0 else float("-inf")
            aRight = A[mid + 1] if (mid + 1) < len(A) else float("inf")
            bLeft = B[j] if j >= 0 else float("-inf")
            bRight = B[j + 1] if (j + 1) < len(B) else float("inf")

            # partition is correct
            if aLeft <= bRight and bLeft <= aRight:
                if total % 2 == 1:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2.0
            elif aLeft > bRight: # => we need to decrease elements in A
                r = mid - 1
            else: # bLeft > aRight => we need more elements from A
                l = mid + 1 # 
        return -1

