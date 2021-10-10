class Solution(object):
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def my_reverse(lst, start, end):
            while start < end:
                temp = lst[start]   
                lst[start] = lst[end]
                lst[end] = temp
                start += 1
                end -= 1
            
        length = len(nums)
        k = k % length
        my_reverse(nums, 0, length - 1)
        my_reverse(nums, 0, k- 1)
        my_reverse(nums, k, length - 1)