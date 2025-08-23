class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        direction = 0 # 0-> right, 1 -> down, 2 -> left, 3 -> up
        result = []
        numElements = len(matrix) * len(matrix[0])

        curr = [0, 0] # x, y coordinate system
        while len(result) != numElements:
            result.append(matrix[curr[1]][curr[0]])
            if direction == 0:
                if curr[0] + 1 > right:
                    direction = 1
                    curr[1] += 1
                    top += 1
                else:
                    curr[0] += 1
            elif direction == 1:
                if curr[1] + 1 > bottom:
                    direction = 2
                    curr[0] -= 1
                    right -= 1
                else:
                    curr[1] += 1
            elif direction == 2:
                if curr[0] - 1 < left:
                    direction = 3
                    curr[1] -= 1
                    bottom -= 1
                else:
                    curr[0] -= 1
            else:
                if curr[1] - 1 < top:
                    direction = 0
                    curr[0] += 1
                    left += 1
                else:
                    curr[1] -= 1
        return result