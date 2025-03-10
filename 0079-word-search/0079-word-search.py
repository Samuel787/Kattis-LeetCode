class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.path = set()
        self.board = board
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(row, col, word):
                    return True
        return False

    
    def dfs(self, row, col, word):
        if len(word) == 0:
            return True
        if (row, col) in self.path:
            return False
        if row < 0 or col < 0 or row >= len(self.board) or col >= len(self.board[0]):
            return False
        if word[0] != self.board[row][col]:
            return False
        self.path.add((row, col))
        # check left
        left = self.dfs(row, col - 1, word[1:])
        if left:
            return True
        # check up
        up = self.dfs(row - 1, col, word[1:])
        if up:
            return True
        # check down
        down = self.dfs(row + 1, col, word[1:])
        if down:
            return True
        # check right
        right = self.dfs(row, col + 1, word[1:])
        if right:
            return True
        self.path.remove((row, col))
        return False

                