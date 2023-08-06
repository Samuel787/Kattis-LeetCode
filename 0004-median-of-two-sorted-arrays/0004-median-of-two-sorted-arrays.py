class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        isNums1Smaller = len(nums1) < len(nums2)
        list1 = nums1 if isNums1Smaller else nums2
        list2 = nums2 if isNums1Smaller else nums1

        totalElements = len(nums1) + len(nums2)
        half = totalElements // 2

        leftIdx, rightIdx = 0, len(list1) - 1
        print("infinity: " + str(float("infinity")))
        # time complexity: Log(min(n, m))
        while True:
            midFirst = (leftIdx + rightIdx) // 2
            midSecond = half - (midFirst + 1) - 1

            # using if conditions to check out of bounds
            list1Left = list1[midFirst] if midFirst >= 0 else float("-infinity")
            list1Right = list1[midFirst + 1] if (midFirst + 1) < len(list1) else float("infinity")
            
            list2Left = list2[midSecond] if midSecond >= 0 else float("-infinity")
            list2Right = list2[midSecond + 1] if (midSecond + 1) < len(list2) else float("infinity")

            # partition is correct
            if list1Left <= list2Right and list2Left <= list1Right:
                # odd
                if totalElements % 2 == 1:
                    return min(list1Right, list2Right) # both will not be equal to infinity
                # even
                else:
                    return (max(list1Left, list2Left) + min(list1Right, list2Right)) / 2.0
            elif list1Left > list2Right: 
                rightIdx = midFirst - 1 # too many elements from list1 in leftPartition
            else:
                leftIdx = midFirst + 1 # too little elements from list1 in leftPartition

