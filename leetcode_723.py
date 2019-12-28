'''
This problem can be solved in 3 steps.
  1. find all the consecutive three or more candies with the same type in a row or in a column and record them in a set.
  2. Change their's value to 0.
  3. Use two pointers to simulate the drop of candies, namly move these elements with non-zero value to the bottom.
Then we just need to call this function recursively until there are no more consecutive candies. 
'''


class Solution(object):
    
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        
        s = set([])
        for i in range(len(board)-2):
            for j in range(len(board[0])):
                if board[i][j] == board[i+1][j] == board[i+2][j] != 0:
                    s.add((i, j))
                    s.add((i+1, j))
                    s.add((i+2, j))
        
        for i in range(len(board)):
            for j in range(len(board[0])-2):
                if board[i][j] == board[i][j+1] == board[i][j+2] != 0:
                    s.add((i, j))
                    s.add((i, j+1))
                    s.add((i, j+2))
        
        for position in s:
            i, j = position[0], position[1]
            board[i][j] = 0
                
                
        for n in range(len(board[0])):
            p1 = len(board)-1
            p2 = len(board)-1
            while p2 >= 0:
                if board[p2][n] != 0:
                    board[p1][n] = board[p2][n]
                    p1 -= 1
                p2 -= 1
            while p1 >= 0:
                board[p1][n] = 0
                p1 -= 1
                
        
        if s:
            self.candyCrush(board)
                
        return board
                                    
        
