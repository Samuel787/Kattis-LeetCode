class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])
        up = 0
        down = rows - 1
        if target < matrix[0][0] or target > matrix[rows - 1][cols - 1]:
            return False
        while up <= down:
            mid = (up + down) / 2
            if target >= matrix[mid][0] and target <= matrix[mid][cols - 1]:
                return self.binarySearch(matrix, mid, target)
            elif target < matrix[mid][0]:
                down = mid - 1
            else:
                up = mid + 1
        return False
    
    def binarySearch(self, matrix, row, target):
        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) / 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False