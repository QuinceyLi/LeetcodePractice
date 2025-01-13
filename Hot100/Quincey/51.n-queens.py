#
# @lc app=leetcode.cn id=51 lang=python3
# @lcpr version=30204
#
# [51] N 皇后
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = [0] * n
        ans = []
        def valid(i,c):
            for r in range(i):
                cc = col[r]
                if cc + r == i + c or cc -r == c - i: return False
            return True
        def dfs(i, s):
            if i == n:
                ans.append(['.'*c + 'Q' + '.'*(n-1-c) for c in col])
                return
            
            for c in s:
                if valid(i, c):
                    col[i] = c
                    dfs(i+1, s-{c})
        dfs(0, set(range(n)))
        return ans
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

