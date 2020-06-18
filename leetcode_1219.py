'''
A typical DFS+backtrack problem. Nothing special here.
'''
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(grid, pos, s, money):
            global res
            money += grid[pos[0]][pos[1]]
            res = max(res, money)
            temp = grid[pos[0]][pos[1]]
            grid[pos[0]][pos[1]] = 0
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for direction in directions:
                x, y = direction
                if 0 <= pos[0]+x < len(grid) and 0 <= pos[1]+y < len(grid[0]) and (pos[0]+x, pos[1]+y) not in s and grid[pos[0]+x][pos[1]+y]:
                    dfs(grid, (pos[0]+x, pos[1]+y), s, money)
            grid[pos[0]][pos[1]] = temp
        
        global res
        res = 0
        s = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    dfs(grid, (i, j), s, 0)
        
        return res
        
