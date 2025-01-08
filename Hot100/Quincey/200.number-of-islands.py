# @lcpr-before-debug-begin
from python3problem200 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30204
#
# [200] 岛屿数量
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j, M, N):
            grid[i][j] = '0' 
            if i+1 < M and grid[i+1][j] == '1':
                grid = dfs(grid,i+1,j,M,N)
            if j+1 < N and grid[i][j+1] == '1':
                grid = dfs(grid,i,j+1,M,N)
            if i-1 >= 0 and grid[i-1][j] == '1':
                grid = dfs(grid,i-1,j,M,N)
            if j-1 >=0 and grid[i][j-1] == '1':
                grid = dfs(grid,i,j-1,M,N)
            return grid
        M, N = len(grid), len(grid[0])
        nisland = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    grid = dfs(grid, i, j, M, N)
                    nisland += 1
        return nisland

# @lc code=end



#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","1"],["0","1","0"],["0","1","0"]]\n
# @lcpr case=end

#

