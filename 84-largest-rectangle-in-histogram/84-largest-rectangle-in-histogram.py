class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        mStack = []
        max_area = 0
        for i in range(len(heights)):
            curr_height = heights[i]
            if not mStack:
                mStack.append([i, curr_height])
                continue
            prev_height = mStack[-1][1]
            start = i
            while curr_height <= prev_height:
                prev_tuple = mStack.pop()
                base = i - prev_tuple[0]
                start = prev_tuple[0]
                # print("base is " + str(base))
                # print("prev height is: " + str(prev_height))
                area = base * prev_height
                max_area = max(max_area, area)
                # print("max_area: " + str(max_area))
                if not mStack:
                    break
                else:
                    prev_height = mStack[-1][1]
            mStack.append([start, curr_height])
            
        # iterate through whatever's left in mStack to also get their area
        for i, h in mStack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
                    
            
            
        