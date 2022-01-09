class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 1
        right = len(height) - 2
        max_left = height[0]
        max_right = height[-1]
        left_arr = []
        right_arr = []
        right_max = -1
        left_max = -1
        for i in height:
            if i > left_max:
                left_max = i
            left_arr.append(left_max)
        for i in reversed(height):
            if i > right_max:
                right_max = i
            right_arr.insert(0, right_max)
        water_count = 0
        for i in range(len(height)):
            curr_water_count = min(left_arr[i], right_arr[i]) - height[i]
            if curr_water_count > 0:
                water_count += curr_water_count
        return water_count
        
        water_count = 0
        # while left < right:
        #     if height[left] <= height[right]:
        #         curr_water_count = min(max_left, max_right) - height[left]
        #         print("iteration >> max_left " + str(max_left) + " max_right " + str(max_right) + " heigh[left]: " + str(height[left]))
        #         if curr_water_count > 0:
        #             water_count += curr_water_count
        #         if height[left] > max_left:
        #             max_left = height[left]
        #         print("index: " + str(left) + " and water count is: " + str(curr_water_count))
        #         left += 1
        #     else:
        #         curr_water_count = min(max_left, max_right) - height[right]
        #         if curr_water_count > 0:
        #             water_count += curr_water_count
        #         if height[right] > max_right:
        #             max_right = height[right]
        #         print("index: " + str(right) + " and water count is: " + str(curr_water_count))
        #         right -= 1
        # return water_count