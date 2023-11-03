class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        height = len(board)
        width = len(board[0])

        for y in range(height):
            for x in range(width):
                if self.searchString(board, x, y, word):
                    return True
        return False

    
    def searchString(self, board, x, y, substring):
        if len(substring) == 0:
            return True
        
        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
            return False

        if board[y][x] != substring[0]:
            return False
        
        board[y][x] = "-1"
        newString = substring[1:] 
        res = self.searchString(board, x - 1, y, newString) or self.searchString(board, x + 1, y, newString) or self.searchString(board, x, y - 1, newString) or self.searchString(board, x, y + 1, newString)
        board[y][x] = substring[0]
        return res
        # print("x: " + str(x) + " y: " + str(y) + "current string :=> " +  substring)
        
        # # left
        # if x > 0:
        #     if self.searchString(board, x - 1, y, newString):
        #         return True
        # # right
        # if x + 1 < len(board[0]):
        #     if self.searchString(board, x + 1, y, newString):
        #         return True 
        # # up
        # if y > 0:
        #     if self.searchString(board, x, y - 1, newString):
        #         return True
        # # down
        # if y + 1 < len(board):
        #     if self.searchString(board, x, y + 1, newString):
        #         return True

        

        # return False
        