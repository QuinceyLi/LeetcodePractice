# @lcpr-before-debug-begin
from python3problem70 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=30204
#
# [70] 爬楼梯
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(k):
            if k == 2: return 2
            elif k == 1: return 1
            return dp(k-1) + dp(k-2)
 
        return dp(n) if n > 2 else n
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

