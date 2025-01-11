# @lcpr-before-debug-begin
from python3problem22 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30204
#
# [22] 括号生成
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        L = 2*n
        ans = []
        path = [''] * L
        def dfs(i, nl, nr):
            if nr > nl: return
            elif nl == n: 
                for k in range(i, L): path[k] = ')'
                ans.append(''.join(path.copy()))
                return
            for idx, c in enumerate(['(', ')']):
                path[i] = c
                dfs(i+1, nl + (1-idx), nr + idx)
        dfs(0, 0, 0)
        return ans

# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

