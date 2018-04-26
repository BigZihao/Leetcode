## O(m * n * l) O(l)

## It's graph instead of path, need to use the visited 

class Solution(object):
<<<<<<< HEAD
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i<0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        res = self.dfs(board, i+1,j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1 , word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
                
=======
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.exist_helper(board, word, i, j):
                    return True
        return False

    def exist_helper(self, board, word, i, j):
        if board[i][j] == word[0]:
            if not word[1:]:
                return True
            board[i][j] = " " # indicate used cell
            # check all adjacent cells
            if i > 0 and self.exist_helper(board, word[1:], i-1, j):
                return True
            if i < len(board)-1 and self.exist_helper(board, word[1:], i+1, j):
                return True
            if j > 0 and self.exist_helper(board, word[1:], i, j-1):
                return True
            if j < len(board[0])-1 and self.exist_helper(board, word[1:], i, j+1):
                return True
            board[i][j] = word[0] # update the cell to its original value
            return False
        else:
            return False
>>>>>>> 9b7f4ed2e579c15e3e1585807828a61ba87f84c0
